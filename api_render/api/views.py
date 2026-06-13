from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "mensagem": "API Django funcionando"
    })
