from django.shortcuts import render
from .forms import Upload_File
from django.core.files.storage import default_storage
from io import StringIO
import fitz
import PyPDF2
import pyttsx3
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_text
import pytesseract   #classic use of AI technique in image processing and text recognition
from PIL import Image
import os
from functools import lru_cache
from pdf2image import convert_from_bytes, convert_from_path
#import re
import uuid
import time
import threading
import pyttsx3
import PyPDF2
pytesseract.pytesseract.tesseract_cmd = r"D:\\chat_botproject\\chatvenv\\Lib\\site-packages\\tesseract\\tesseract.exe"

#home page view
def hello(request):
    return render(request, "home.html")

#Check if a PDF contains selectable text.
def is_pdf_contain_text(pdf_path):
    #extract_text() function from pdfminer
    text = extract_text(pdf_path)   #extract any text present in the PDF file at pdf_path
    return bool(text.strip())       #True if any text is present False if the text is empty means no selectable text

#Check if a PDF contains images
def is_pdf_contain_images(pdf_path):
    #error handling required to catch errors while processing the PDF files.
    try:
        doc = fitz.open(pdf_path)   #helps in opening PDF doc
        print(doc)
        #iterates through each page of the PDF
        for page_num in range(len(doc)):
            print(page_num)
            page = doc.load_page(page_num)   #loading page from PDF
            print(page)
            #Checking if the current page contains any images
            if page.get_images():
                return True  #if img found it returns true value
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False
    return False   #if no images are found or an error occurs,returns False

@lru_cache(maxsize=70)
def pdf_to_txt(request):
    start_time = time.time()  #Recording the current time to measure the time taken for the entire operation
    context = {'files': []}   #holds info about processed pdf files

    if request.method == 'POST':      #checks if method is POST
        form = Upload_File(request.POST, request.FILES)
        if form.is_valid():   #Checks if the form is valid that the form fields and file uploads meet the required criteria.
            pdf_files = form.cleaned_data["pdf"]   #Retrieves the cleaned data from the form
            #Loops through each uploaded PDF file
            for pdf_file in pdf_files:
                #Saves the uploaded PDF file to the default Django storage backend. It creates a unique filename using uuid.uuid4() to avoid file name collisions.
                temp_file_path = default_storage.save(f'temp_{uuid.uuid4()}.pdf', pdf_file)
                temp_file_path = default_storage.path(temp_file_path) #Retrieves the full file path for the saved temporary file.
                file_context = {'name': pdf_file.name,'text': ''}
                #try-except block to catch any errors during the PDF text extraction
                try:
                    #previous function calling to check the text is selectable or not
                    if is_pdf_contain_text(temp_file_path):
                        output_string = StringIO()  #creates an in-memory file object that can be used to store extracted text.
                        with open(temp_file_path, 'rb') as pdf: #opens the PDF file in binary read mode
                            parser = PDFParser(pdf)  #creates a PDF parser object that reads the raw data from the PDF file
                            doc = PDFDocument(parser)  #parses the document structure from the parser
                            rsrcmgr = PDFResourceManager() #creates a resource manager that stores shared resources, such as fonts and images
                            laparams = LAParams()  #sets layout parameters to control how the text layout is analyzed
                            #converts the PDF content into text format and stores it in output_string
                            device = TextConverter(rsrcmgr, output_string, laparams=laparams) 
                            interpreter = PDFPageInterpreter(rsrcmgr, device) #creates a page interpreter to process each page in the PDF
                            #iterates through each page of the PDF
                            for page in PDFPage.create_pages(doc):
                                interpreter.process_page(page)  #processes the page to extract the text
                            text = output_string.getvalue()  #extracts the text from the StringIO object
                        file_context['text'] = text  #stores the extracted text in the dictionary
                    #if the PDF doesn’t contain text but contains images, this block is executed
                    elif is_pdf_contain_images(temp_file_path):
                        images = convert_from_path(temp_file_path) #converts each page of the PDF into an image using pdf2image
                        text = ''  #initializes an empty string to hold text extracted from images
                        #Loops through each image page of the PDF
                        for image in images:
                            #extracts text from the image using pytesseract (OCR) and appends it to the text string
                            text += pytesseract.image_to_string(image) #AI
                        file_context['text'] = text  #stores the extracted OCR text
                #if any error occurs during the PDF processing, it is caught here
                except Exception as e:
                    file_context['error'] = f"An unexpected error occurred: {str(e)}"
                #finally to ensure the temporary file is deleted
                finally:
                    if os.path.exists(temp_file_path):  #checks if the temporary file still exists
                        os.remove(temp_file_path)  #deletes the temporary PDF file

                context['files'].append(file_context)  #Adds the file_context dictionary to the files list in the context dictionary
                end_time = time.time() #records the time when processing finishes
                print(f"total time : {start_time-end_time} seconds")
            return render(request, 'pdf.html', context)
        else:
            context['error'] = 'Invalid form'
    else:
        form = Upload_File()
    context['form'] = form
    return render(request, 'pdf.html', context)

#text to speech functionality
#global variable to manage pyttsx3 text-to-speech engine
engine = None
stop_event = threading.Event()  #object to manage when to stop the text-to-speech engine

#Start reading the given text using pyttsx3
def start_reading(text):
    global engine
    stop_event.clear()  #clears any previous stop signals so that the reading can start again
    engine = pyttsx3.init()  #initializing engine every time a new request is made
    engine.say(text)
    
    try:
        engine.runAndWait()  #run the engine and wait till the text is read or stop is triggered
    except Exception as e:
        print(f"Engine Error: {e}")
    finally:
        engine.stop()  #make sure engine stops after completion

#Stop the reading by setting the stop event
def stop_reading_pdf():
    global engine
    stop_event.set()  #set the stop event to stop the reading
    if engine:
        engine.stop()  #stopz the pyttsx3 engine

#handles the text-to-speech reading of an uploaded PDF
def ReadPdf(request):
    global engine, stop_event

    if request.method == 'POST':
        #if the user clicks the stop button, it triggers stop_reading_pdf() to halt the text-to-speech process
        if 'stop' in request.POST:
            stop_reading_pdf()  # Trigger the stop if the stop button is clicked
            return render(request, 'read.html', {'message': 'Reading stopped.'})
        
        pdf_file = Upload_File(request.POST, request.FILES)
        if pdf_file.is_valid():
            pdf_file = request.FILES['pdf'] #retrieves the uploaded PDF file
            name = pdf_file.name
            pdf_reader = PyPDF2.PdfReader(pdf_file)  #reads the uploaded PDF file using PyPDF2
            text = ''

            #loops through each page of PDF
            for page_num in range(len(pdf_reader.pages)):
                if stop_event.is_set():  # If stop is triggered, exit the loop
                    break
                page = pdf_reader.pages[page_num]
                text += page.extract_text()  #extracts text from the current page and appends it to the text string

            #context to pass to the template
            context = {'name': name, 'text': text}

            #starts reading the PDF in a separate thread
            reading_thread = threading.Thread(target=start_reading, args=(text,))
            reading_thread.start()
            return render(request, 'read.html', context)
    return render(request, 'read.html', {'pdf_file': Upload_File()})
