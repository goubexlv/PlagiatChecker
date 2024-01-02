from django.shortcuts import render
from pdfminer.high_level import extract_text
from django.http import JsonResponse


# Create your views here.


def plagiatOnline(request):
    return render(request, "online/index.html")

def upload_file(request):
    if request.method == 'POST':
        try:
            # uploaded_file = request.FILES.get('file')
            uploaded_file = request.FILES.get('file')

            # Check if a file was actually uploaded
            if not uploaded_file:
                raise ValueError("A file was not provided.")

            # pdf_content = extract_text_from_pdf(uploaded_file)
          
            # return JsonResponse({'pdf_content': pdf_content})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée.'}, status=405)
                
def extract_text_from_pdf(uploaded_file):
    # Extract text from the PDF file
    try:
        pdf_content = extract_text(uploaded_file)
    except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return pdf_content