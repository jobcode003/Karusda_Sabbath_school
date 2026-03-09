from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def register_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            phone_number = form.cleaned_data.get('phone_number')
            
            # Check for existing member with same first name and phone number
            existing_member = Member.objects.filter(
                first_name__iexact=first_name, 
                phone_number=phone_number
            ).first()
            
            if existing_member:
                existing_member.registration_count += 1
                existing_member.save()
                messages.success(request, f'Welcome back, {first_name}! Your registration has been updated (Count: {existing_member.registration_count}).\nHave a Blessed Sabbath.')
            else:
                form.save()
                messages.success(request, 'Registration successful! \nHave a Blessed Sabbath.')
            
            return redirect('register_member')
    else:
        form = MemberForm()
    
    return render(request, 'register.html', {'form': form})
