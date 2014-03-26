function salvarUsuario() {
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
    } else {
        $.ajax({
            url: '/usuario/crud/salvar',
            type: 'POST',
            data: $('#form_usuario').serialize(),
            success: function(result) {
                alert('Usuário cadastrado com sucesso');
                window.location.href = '/'
            }
        })
    }
}
