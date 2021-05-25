// Updates the total cost of a custom built PC as user is picking components
$(document).ready(function () {
    $('#custom-build-form').change(function() {
        var selectedCasePrice = parseFloat($('#cases').find(":selected").data('price')) || 0.00;
        var selectedMotherboardPrice = parseFloat($('#motherboard').find(":selected").data('price')) || 0.00;
        var selectedCpuPrice = parseFloat($('#cpus').find(":selected").data('price')) || 0.00;
        var selectedGpuPrice = parseFloat($('#gpus').find(":selected").data('price')) || 0.00;
        var selectedMemoryPrice = parseFloat($('#memory').find(":selected").data('price')) || 0.00;
        var selectedStoragePrice = parseFloat($('#storage').find(":selected").data('price')) || 0.00;
        var selectedPsuPrice = parseFloat($('#psus').find(":selected").data('price')) || 0.00;
        var selectedCoolingPrice = parseFloat($('#cooling').find(":selected").data('price')) || 0.00;

        var currentPrice = parseFloat((selectedCasePrice + selectedMotherboardPrice + selectedCpuPrice + selectedGpuPrice + selectedMemoryPrice + selectedCoolingPrice + selectedPsuPrice + selectedStoragePrice).toFixed(2));
        document.getElementById('current-price').innerHTML = currentPrice;
    });
});