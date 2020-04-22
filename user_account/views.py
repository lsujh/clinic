from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddPetsForm
from .models import Pets


@login_required
def all_pets_user(request):
    pets = Pets.objects.filter(UserId=request.user)
    for pet in pets:
        print(pet)
    return render(request, 'user_account/all_pets_user.html', {'pets': pets})


@login_required
def add_pet(request):
    if request.method == 'POST':
        pet_form = AddPetsForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('user_account:all_pets_user')
    else:
        pet_form = AddPetsForm()
    return render(request, 'user_account/add_pet.html', {'pet_form': pet_form})


@login_required
def edit_pet(request, id):
    data = get_object_or_404(Pets, PetId=id, UserId=request.user)
    if request.method == 'POST':
        pet_form = AddPetsForm(request.POST, request.FILES, instance=data)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('user_account:all_pets_user')
    else:
        pet_form = AddPetsForm(initial={'PetName':data.PetName, 'DateOfBirth': data.DateOfBirth,
                                        'PetSex': data.PetSex, 'PetTypeId': data.PetTypeId,
                                        'BreedId': data.BreedId, 'Weight': data.Weight,
                                        'Image': data.Image})
    return render(request, 'user_account/edit_pet.html', {'pet_form': pet_form})


@login_required
def delete_pet(request, id):
    pet_data = Pets.objects.filter(PetId=id)
    if request.method == 'POST':
        pet_data.delete()
        return redirect('user_account:all_pets_user')
    else:
        return render(request, 'user_account/delete_pet.html', {'pet_data': pet_data})












