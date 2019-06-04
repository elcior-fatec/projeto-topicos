from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from filtro_cnae.models import SearchedCNAE


@login_required
def pesquisa_user(request):
    pesquisas = SearchedCNAE.objects.filter(id_user=request.user.id)
    return render(request, 'pesquisas-user.html', {'pesquisas': pesquisas})


@login_required
def deletar_pesquisa(request, id):
    pesquisa = get_object_or_404(SearchedCNAE, pk=id)
    if request.method == 'POST':
        pesquisa.delete()
        return redirect('pesquisa_user')
    return render(request, 'confirmar-delete-pesquisa.html', {'pesquisa': pesquisa})


@login_required
def detalhar_pesquisa(request, id):
    pesquisa = get_object_or_404(SearchedCNAE, pk=id)
    return render(request, 'detalhe-pesquisa.html', {'pesquisa': pesquisa})
