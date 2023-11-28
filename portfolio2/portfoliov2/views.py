from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalInfo, Project, BlogPost, Newsletter
import os, csv
from django.conf import settings
# from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail
from string import Template
from pathlib import Path

from django.db.models import Q
from itertools import chain
from django.template.loader import render_to_string

from portfoliov2.forms import ContactMessageForm, SubscriberForm  # Import the ModelForm
from reportlab.pdfgen import canvas  #For Subscribers PDF generation

# Create your views here.

def common_data(request):

    personal_info = PersonalInfo.objects.first()
    education = personal_info.education.all()
    internship = personal_info.internship.all()
    tech_stack = personal_info.tech_stack.all()

    projects = Project.objects.all()

    # Search bar code begins
    # search_query = request.GET.get('query', '')
    search_query = request.GET.get('search_query') if request.GET.get('search_query') != None else ''

    # Perform separate search queries for each model
    search_results_education = personal_info.education.filter(
        Q(institution__icontains=search_query) |
        Q(degree__icontains=search_query) |
        Q(description__icontains=search_query)
    )
    
    search_results_internship = personal_info.internship.filter(
        Q(company__icontains=search_query) |
        Q(role__icontains=search_query) |
        Q(description__icontains=search_query)
    )
    
    search_results_tech_stack = personal_info.tech_stack.filter(
        Q(name__icontains=search_query)
    )
 
    search_results_project = Project.objects.filter(
        Q(title__icontains=search_query) |
        Q(category__icontains=search_query)
    )

    search_results_blog_post = BlogPost.objects.filter(
        Q(category__icontains=search_query) |
        Q(post_author__icontains=search_query) |
        Q(post_title__icontains=search_query)
    )

    # Combine the QuerySets
    search_results = list(
        chain(
            search_results_education,
            search_results_internship,
            search_results_tech_stack,
            search_results_project,
            search_results_blog_post,
        )
    )

    # Search bar code ends

    # Subscriber starts
    subs_form = None
    if request.method == 'POST':
        subs_form = SubscriberForm(request.POST)
        if subs_form.is_valid():
            # subs_form.save()
            # Check if the subscriber's email already exists in the database
            subscriber_email = subs_form.cleaned_data.get('email', '')

            try:
                if not Newsletter.objects.filter(email=subscriber_email).exists():
                    # If it doesn't exist, save the subscriber and update the file, CSV, and PDF
                    subs_form.save()
                
                
                    # subscriber = subs_form.cleaned_data['email']

                    # Append to SubscribersList.txt
                    file_path = os.path.join(settings.MEDIA_ROOT, 'SubscribersList.txt' )
                    try:
                        with open(file_path, mode='a') as file:
                            
                            file.write(subscriber_email + ',\n')  # Write the subscriber's email followed by a comma and a new line

                    except IOError as e:
                        print(f"Error writing to file: {e}")

                    # Append to SubscribersList.csv
                    csv_file_path = os.path.join(settings.MEDIA_ROOT, 'SubscribersList.csv')
                    try:
                        with open(csv_file_path, mode='a', newline='') as csv_file:
                            csv_writer = csv.writer(csv_file)
                            csv_writer.writerow([subscriber_email  + ','])  # Write the email as a single-row list
                    except IOError as e:
                        print(f"Error writing to SubscribersList.csv: {e}")

                    # Append to SubscribersList.pdf
                    pdf_file_path = os.path.join(settings.MEDIA_ROOT, 'SubscribersList.pdf')
                    try:
                        c = canvas.Canvas(pdf_file_path)
                        c.setFont('Helvetica', 12)
                        c.drawString(20, 900, subscriber_email + ',')  # Write the email followed by a comma at the specified position
                        c.showPage()
                        c.save()
                    except IOError as e:
                        print(f"Error writing to SubscribersList.pdf: {e}")

                    messages.success(request, 'Email added successfully.')
                    # return JsonResponse({'message': 'success'})
                else:
                    # If the email already exists, show an error message
                    messages.error(request, 'Email already exists in the newsletter.')
                    # return JsonResponse({'message': 'error'})
            
            except Exception as e:
                # Handle other exceptions and set an error message
                messages.error(request, f'An error occurred: {str(e)}')
                # return JsonResponse({'message': 'error'})

            # return JsonResponse({'message': 'success' if subs_form.is_valid() else 'error'})
                # return redirect('home')

    else:
        subs_form = SubscriberForm()
    # Subscriber ends 

    # Blog Starts
    blogs = BlogPost.objects.all().order_by('-post_date')[:10]
    # Blog Ends
    # print(personal_info.twitter_link)

    return {
        'personal_info': personal_info,
        'education': education,
        'internship': internship,
        'tech_stack': tech_stack,
        'projects': projects,
        'blogs': blogs,
        'subs_form': subs_form,
        'search_results':search_results,
        'search_query': search_query,
    }

    # if search_query:
    #     return render(request, 'portfoliov2/search_results.html', context)
    # else:

def home(request):

    context_data = common_data(request) 
    # print(context_data.search_results)  
    return render(request, 'portfoliov2/home.html', context_data)

def contactus(request): 
    form = None
    contactt = None
    # subscriber = None

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            contactt = form.save(commit=False)

            contactt.save()
            name = contactt.name
            mail = contactt.email
            subject = contactt.title
            message = contactt.message

            # Addition to subscriber form starts
            # Check if the email already exists in the Newsletter model
            check_email_exists = Newsletter.objects.filter(email=contactt.email).exists()

            if not check_email_exists:
                # If the email doesn't exist, add it to the Newsletter model
                subscriber_form = SubscriberForm({'email': contactt.email})
                if subscriber_form.is_valid():
                    subscriber_form.save()
            # Addition to subscriber form ends

            # html = Template(Path('portfoliov2/contactmessage.html').read_text())
            # email = EmailMessage()
            # email['from'] = settings.EMAIL_HOST_USER
            # email['to'] = ['allschoolsinfo1@gmail.com', 'abdulahogundare21@gmail.com']
            # email['subject'] = contactt.title
            # email.content_subtype = 'html'
            # email.set_content(html.safe_substitute({'name': name, 'title': title, 'message': message, 'mail': mail}))

            # with smtplib.SMTP('smtp-relay.brevo.com', 587) as smtp:
            #     smtp.ehlo()
            #     smtp.starttls()
            #     smtp.ehlo()
            #     smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            #     smtp.send_message(email)
            #     print('Message sent, Any other task?')
            
            # # Add a success message
            # messages.success(request, 'Your message has been sent successfully!')

            # Construct email content directly
            email_content =  f""" Their's a mail from {name} \n \n {message} \n \n \n Reply to: {mail}"""
            # body = email_content
            # # Create EmailMessage object
            # email = EmailMessage(
            #     subject,
            #     body=body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=['allschoolsinfo1@gmail.com', 'abdulahogundare21@gmail.com'],
            # )
            

            try:
                # Send the email using send_mail
                send_mail(
                    subject,
                    email_content,
                    settings.EMAIL_HOST_USER,
                    ['allschoolsinfo1@gmail.com', 'abdulahogundare@gmail.com'],
                    fail_silently=False,  # Set to True for production
                )

                messages.success(request, 'Your message has been sent successfully!')
                print('Message sent, Any other task?')
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')
                print(f'Error sending email: {str(e)}')


            # Optional: Attach files if needed
            # email.attach_file('/path/to/attachment.txt')

            # Optional: Add headers or extra info
            # email.extra_headers['Message-ID'] = 'custom-message-id'

            # try:
            #     # Send the email
            #     email.send()
            #     messages.success(request, 'Your message has been sent successfully!')
            #     print('Message sent, Any other task?')
            # except Exception as e:
            #     messages.error(request, f'Error sending email: {str(e)}')
            #     print(f'Error sending email: {str(e)}')

            # return redirect('home')
    else:
        form = ContactMessageForm()
    # Contact form ends

    context_data = common_data(request)
    contact_form_data = {'form': form}
    context_data.update(contact_form_data)        
    return render(request, 'portfoliov2/contactus.html', context_data)


def blog(request):
    blogs = BlogPost.objects.all().order_by('-post_date')

    context_data = common_data(request)
    blogs_data = {'blogs': blogs}
    context_data.update(blogs_data)  
    return render(request, 'portfoliov2/blog.html', context_data)


def blog_single_post(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)

    context_data = common_data(request)
    blogpost_data = {'blogpost': blogpost}
    context_data.update(blogpost_data)    
    return render(request, 'portfoliov2/blogpost.html', context_data)
