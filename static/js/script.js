// Função para confirmar a exclusão de um item
function confirmarExclusao() {
    return confirm("Você tem certeza que deseja excluir este item?");
}

// Função para validação básica de formulários
function validarFormulario() {
    const nome = document.getElementById("nome").value;
    const empresa = document.getElementById("empresa").value;

    if (!nome || !empresa) {
        alert("Todos os campos são obrigatórios!");
        return false;
    }
    return true;
}
