from django.shortcuts import render

finches = [
    {
        'species': 'Zebra Finch',
        'scientific_name': 'Taeniopygia guttata',
        'description': 'The zebra finch is a small, colorful bird native to Australia. They are popular as pets due to their cheerful disposition and melodious song. Zebra finches are highly social and often found in large flocks in the wild.',
        'habitat': 'Grasslands, forests, and urban areas',
        'diet': 'Mainly seeds, supplemented with insects and fruits',
        'average_lifespan': '5 to 7 years',
        'image_url': 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/123646541/1800'
    },
    {
        'species': 'Gouldian Finch',
        'scientific_name': 'Erythrura gouldiae',
        'description': 'The Gouldian finch, also known as the rainbow finch, is a strikingly colored bird native to northern Australia. It is highly sought after by aviculturalists for its vibrant plumage, which comes in various color mutations.',
        'habitat': 'Savannah woodlands and grasslands',
        'diet': 'Mainly grass seeds, supplemented with insects',
        'average_lifespan': '6 to 8 years',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Male_adult_Gouldian_Finch.jpg/640px-Male_adult_Gouldian_Finch.jpg'
    },
    {
        'species': 'Society Finch',
        'scientific_name': 'Lonchura domestica',
        'description': 'The society finch, also known as the Bengalese finch, is a small, hardy bird that has been domesticated for centuries. It is a popular choice for novice bird keepers due to its ease of care and sociable nature.',
        'habitat': 'Originally from Asia, now domesticated worldwide',
        'diet': 'Seeds, greens, and occasional insects',
        'average_lifespan': '5 to 7 years',
        'image_url': 'https://www.serenityusa.com/app/uploads/2023/10/society-finch-perched-outside.jpg'
    },
    {
        'species': 'Java Sparrow',
        'scientific_name': 'Lonchura oryzivora',
        'description': 'Although commonly referred to as a sparrow, the Java sparrow is actually a species of finch native to Java, Indonesia. It is known for its bold black-and-white plumage and distinctive pink bill.',
        'habitat': 'Grasslands, agricultural fields, and urban areas',
        'diet': 'Mainly seeds, with some greens and insects',
        'average_lifespan': '5 to 8 years',
        'image_url': 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/97645141/1800'
    }
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })