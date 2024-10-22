document.addEventListener('DOMContentLoaded', function () {
    const voluntadSelect = document.getElementById('voluntad');
    const codigoPrestadorInput = document.getElementById('codigo_prestador');

    function desabilitarCodigoPrestador() {
        if (voluntadSelect.value === 'No') {
            codigoPrestadorInput.value = '';
            codigoPrestadorInput.disabled = true;
            codigoPrestadorInput.required = false;
        } else {
            codigoPrestadorInput.disabled = false;
            codigoPrestadorInput.required = true;
        }
    }

    desabilitarCodigoPrestador();

    voluntadSelect.addEventListener('change', desabilitarCodigoPrestador);

});
