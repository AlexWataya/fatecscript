function salvarLanche() {
    if (!verificarErros()) {
        $.ajax({
            url: '/cardapio/crud/salvar_lanche',
            type: 'POST',
            data: $('#form_cardapios').serialize(),
            success: function(result) {
                alert('Lanche cadastrado com sucesso');
                window.location.href = '/cardapio/crud/cardapio_listar'
            }
        })
    }
}

function verificarErros() {
    var msg = '';
    $('.required').each(function() {
        if ($(this).val() == '') {
            var labelText = $(this).prev().text()
            msg = msg + labelText.substr(0, labelText.length - 1) + ' é obrigatório. <p />';
        }
    })
    if (msg != '') {
        $('.view').removeClass('hide');
        $('#msg_error').html(msg);
        return true;
    }
    return false;
}