function salvarUsuario() {
     if (!verificarErros()) {
        $.ajax({
            url: '/usuario/crud/salvar',
            type: 'POST',
            data: $('#form_usuario').serialize(),
            success: function(result) {
                alert('Usuário cadastrado com sucesso');
                window.location.href = '/usuario/crud/usuario_listar'
            }
        })
    }
}

function salvarCardapio() {
    if (!verificarErros()) {
        $.ajax({
            url: '/usuario/crud/salvarCardapio',
            type: 'POST',
            data: $('#form_cardapios').serialize(),
            success: function(result) {
                alert('Cardápio cadastrado com sucesso');
                window.location.href = '/usuario/crud/cardapio_listar'
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

