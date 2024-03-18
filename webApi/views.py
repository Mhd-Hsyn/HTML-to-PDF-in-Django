import io, json
from django.http import HttpResponse
from rest_framework.response import Response

## use reportlab for pdf generator
# from reportlab.pdfgen import canvas
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from xhtml2pdf import pisa   #also use in reportlab

# WesayPrint TO generate pdf
from weasyprint import HTML

# FOr merge 2 pdfs
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO


from rest_framework.views import APIView
from .Useable import useable as uc


from django.template import Context, Template

from .models import *
from .serializers import *

# BEST LIBRARY FOR PDF use this library (PDF KIT)
import pdfkit


# class GeneratePDF(APIView):
#     def get(self, request, *args, **kwargs):
#         data= {

#         }
#         response = uc.generate_pdf(data)
#         if not response['status']:
#             return {'something wents wrong'}
        
#         html = response['pdf_code']
#         # Create a PDF buffer
#         buffer = BytesIO()

#         # Generate PDF
#         pisa.CreatePDF(html, dest=buffer)

#         # Fetch the PDF buffer value
#         pdf_file = buffer.getvalue()
#         buffer.close()

#         # Prepare HTTP response with PDF as attachment
#         response = HttpResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="output.pdf"'
#         return response


class GeneratePDF(APIView):
    def get(self, request, *args, **kwargs):
        data= {
            "author_name": "Hussain",
            "author_address": "Nazimabad"
        }
        response = uc.generate_pdf_summary(data)
        if not response['status']:
            return HttpResponse("Something went wrong while generating the PDF.")
        
        html = response['pdf_code']

        # Generate PDF
        pdf_file1 = HTML(string=html).write_pdf()


        data= {
            "lname": "Hussain",
            "relation_name": "Saqlain",
            "relation": "Brother",
            "relation_dob": "31st Dec 2001",
            "relation_livesin": "Karachi",
            "relation_pob": "Karachi",
            "relation_fav_food": "Biryani",
            "relation_profession": "Frontend Developer",
            "relation_fav_holiday": "Eid ul Azha",
            "relation_fear": "Top Height Building",
            "relation_fav_qoute": "Be Happy . . . ",
            "relation_img": "no img"
        }
        response = uc.generate_pdf_familybios(data)
        if not response['status']:
            return HttpResponse("Something went wrong while generating the PDF.")
        
        html = response['pdf_code']

        # Generate PDF
        pdf_file2 = HTML(string=html).write_pdf()

        # Merge PDF files
        output_pdf = BytesIO()
        pdf_writer = PdfWriter()
        pdf_reader1 = PdfReader(BytesIO(pdf_file1))
        pdf_reader2 = PdfReader(BytesIO(pdf_file2))

        for page in range(len(pdf_reader1.pages)):
            pdf_writer.add_page(pdf_reader1.pages[page])

        for page in range(len(pdf_reader2.pages)):
            pdf_writer.add_page(pdf_reader2.pages[page])

        pdf_writer.write(output_pdf)
        output_pdf.seek(0)

        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(output_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response



class GeneratePDF2(APIView):
    def get(self, request, *args, **kwargs):
        data= {
            "lname": "Hussain",
            "relation_name": "Saqlain",
            "relation": "Brother",
            "relation_dob": "31st Dec 2001",
            "relation_livesin": "Karachi",
            "relation_pob": "Karachi",
            "relation_fav_food": "Biryani",
            "relation_profession": "Frontend Developer",
            "relation_fav_holiday": "Eid ul Azha",
            "relation_fear": "Top Height Building",
            "relation_fav_qoute": "Be Happy . . . ",
            "relation_img": "no img"
        }
        response = uc.generate_pdf_familybios(data)
        if not response['status']:
            return HttpResponse("Something went wrong while generating the PDF.")
        
        html = response['pdf_code']

        # Generate PDF
        pdf_file = HTML(string=html).write_pdf()

        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response




class GeneratePDF3(APIView):
    """
    Use Jinja Template single pdf
    """
    def get(self, request, *args, **kwargs):
        data= {
            "author_name": "Hussain",
            "author_address": "Nazimabad"
        }
        template = Template(open('static/pdfs/summary.html').read())
        context = Context(data)
        html = template.render(context)

        # Generate PDF
        pdf_file = HTML(string=html).write_pdf()
        
        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response




class GeneratePDF4(APIView):
    """
    Use Jinja Template multiple pdf
    """
    def get(self, request, *args, **kwargs):
        data= {
            "author_name": "Hussain",
            "author_address": "Nazimabad"
        }
        template = Template(open('static/pdfs/summary.html').read())
        context = Context(data)
        html = template.render(context)

        # Generate PDF
        pdf_file1 = HTML(string=html).write_pdf()

        data2= {
            "lname": "Hussain",
            "relation_name": "Saqlain",
            "relation": "Brother",
            "relation_dob": "31st Dec 2001",
            "relation_livesin": "Karachi",
            "relation_pob": "Karachi",
            "relation_fav_food": "Biryani",
            "relation_profession": "Frontend Developer",
            "relation_fav_holiday": "Eid ul Azha",
            "relation_fear": "Top Height Building",
            "relation_fav_qoute": "Be Happy . . . ",
            "relation_img": "no img"
        }
        template = Template(open('static/pdfs/familybios.html').read())
        context = Context(data2)
        html = template.render(context)

        # Generate PDF
        pdf_file2 = HTML(string=html).write_pdf()

        # Merge PDF files
        output_pdf = BytesIO()
        pdf_writer = PdfWriter()
        pdf_reader1 = PdfReader(BytesIO(pdf_file1))
        pdf_reader2 = PdfReader(BytesIO(pdf_file2))

        for page in range(len(pdf_reader1.pages)):
            pdf_writer.add_page(pdf_reader1.pages[page])

        for page in range(len(pdf_reader2.pages)):
            pdf_writer.add_page(pdf_reader2.pages[page])

        pdf_writer.write(output_pdf)
        output_pdf.seek(0)

        
        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(output_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response



class GeneratePDF5(APIView):
    """
    Use Query from DB
    """
    def get(self, request, *args, **kwargs):
        
        id = request.GET.get('id', None)
        fetch_family_members= FamilyMember.objects.filter(user= id)
        family_ser_data= FamilyMemberSer(fetch_family_members, many=True, context={'request': request}).data
        print(json.dumps(family_ser_data, indent=2))

        fetch_user = User.objects.filter(id=id).first()
        user_ser_data= UserSerializer(fetch_user).data

        template = Template(open('static/pdfs/summary.html').read())
        context = Context(user_ser_data)
        html = template.render(context)

        # Generate PDF
        pdf_file1 = HTML(string=html).write_pdf()

        template = Template(open('static/pdfs/familybios.html').read())
        context = Context({'family_members': family_ser_data, 'user_lname': user_ser_data['lname']})
        html = template.render(context)

        # Generate PDF
        pdf_file2 = HTML(string=html).write_pdf()

        # Merge PDF files
        output_pdf = BytesIO()
        pdf_writer = PdfWriter()
        pdf_reader1 = PdfReader(BytesIO(pdf_file1))
        pdf_reader2 = PdfReader(BytesIO(pdf_file2))

        for page in range(len(pdf_reader1.pages)):
            pdf_writer.add_page(pdf_reader1.pages[page])

        for page in range(len(pdf_reader2.pages)):
            pdf_writer.add_page(pdf_reader2.pages[page])

        pdf_writer.write(output_pdf)
        output_pdf.seek(0)

        
        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(output_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response
    




# using import pdfkit
# class GeneratePDF6(APIView):
#     """
#     Use Query from DB
#     """
#     def get(self, request, *args, **kwargs):
#         id = request.GET.get('id', None)

#         # Fetch family members
#         fetch_family_members = FamilyMember.objects.filter(user=id)
#         family_ser_data = FamilyMemberSer(fetch_family_members, many=True, context={'request': request}).data
#         print(json.dumps(family_ser_data, indent=2))

#         # Fetch user
#         fetch_user = User.objects.filter(id=id).first()
#         user_ser_data = UserSerializer(fetch_user).data

#         # Render summary HTML
#         template = Template(open('static/pdfs/summary.html').read())
#         context = Context(user_ser_data)
#         html_summary = template.render(context)

#         # Render familybios HTML
#         template = Template(open('static/pdfs/familybios.html').read())
#         context = Context({'family_members': family_ser_data, 'user_lname': user_ser_data['lname']})
#         html_familybios = template.render(context)

#         # Generate PDF from HTML
#         pdf_summary = pdfkit.from_string(html_summary, False)
#         pdf_familybios = pdfkit.from_string(html_familybios, False)

#         # Prepare output PDF
#         output_pdf = BytesIO()

#         # Write the generated PDFs to the output PDF
#         output_pdf.write(pdf_summary)
#         output_pdf.write(pdf_familybios)

#         # Move to the beginning of the output PDF buffer
#         output_pdf.seek(0)

#         # Prepare HTTP response with PDF as attachment
#         response = HttpResponse(output_pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="output.pdf"'
#         return response






# # using import pdfkit      append multiple html
# class GeneratePDF6(APIView):
#     """
#     Use Query from DB
#     """
#     def get(self, request, *args, **kwargs):
#         id = request.GET.get('id', None)

#         # Fetch family members
#         fetch_family_members = FamilyMember.objects.filter(user=id)
#         family_ser_data = FamilyMemberSer(fetch_family_members, many=True, context={'request': request}).data
#         print(json.dumps(family_ser_data, indent=2))

#         # Fetch user
#         fetch_user = User.objects.filter(id=id).first()
#         user_ser_data = UserSerializer(fetch_user).data

#         # Render summary HTML
#         template = Template(open('static/pdfs/summary.html').read())
#         context = Context(user_ser_data)
#         html_summary = template.render(context)

#         # Render familybios HTML
#         template = Template(open('static/pdfs/familybios.html').read())
#         context = Context({'family_members': family_ser_data, 'user_lname': user_ser_data['lname']})
#         html_familybios = template.render(context)

#         # Combine HTMLs
#         combined_html = html_summary + html_familybios

#         # Generate PDF from combined HTML
#         pdf_combined = pdfkit.from_string(combined_html, False)

#         # Prepare HTTP response with PDF as attachment
#         response = HttpResponse(pdf_combined, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="output.pdf"'
#         return response
    






# using import pdfkit      append multiple html with different pages 
class GeneratePDF6(APIView):
    """
    Use Query from DB
    """
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)

        # Fetch family members
        fetch_family_members = FamilyMember.objects.filter(user=id)
        family_ser_data = FamilyMemberSer(fetch_family_members, many=True, context={'request': request}).data
        print(json.dumps(family_ser_data, indent=2))

        # Fetch user
        fetch_user = User.objects.filter(id=id).first()
        user_ser_data = UserSerializer(fetch_user).data

        # Initialize combined HTML string
        combined_html = ''

        # Render summary HTML
        template = Template(open('static/pdfs/summary.html').read())
        context = Context(user_ser_data)
        html_summary = template.render(context)

        # Append summary HTML to combined HTML with a page break
        combined_html += html_summary + '<div style="page-break-after:always;"></div>'

        # Render familybios HTML
        template = Template(open('static/pdfs/familybios.html').read())
        context = Context({'family_members': family_ser_data, 'user_lname': user_ser_data['lname']})
        html_familybios = template.render(context)

        # Append familybios HTML to combined HTML with a page break
        combined_html += html_familybios + '<div style="page-break-after:always;"></div>'

        # Generate PDF from combined HTML
        pdf_combined = pdfkit.from_string(combined_html, False)

        # Prepare HTTP response with PDF as attachment
        response = HttpResponse(pdf_combined, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="output.pdf"'
        return response