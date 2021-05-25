$(document).ready(function () {
    $('#custom-build-form').submit(function (e) {

        e.preventDefault();

        var csrfmiddlewaretoken = $(this).children('input[name=csrfmiddlewaretoken]').val();
        var selectedCase = $('#cases').find(":selected");
        var selectedMotherboard = $('#motherboard').find(":selected");
        var selectedCpu = $('#cpus').find(":selected");
        var selectedGpu = $('#gpus').find(":selected");
        var selectedMemory = $('#memory').find(":selected");
        var selectedStorage = $('#storage').find(":selected");
        var selectedPsu = $('#psus').find(":selected");
        var selectedCooling = $('#cooling').find(":selected");
        var image = selectedCase.data('image');
        var quantity = $(this).children('input[name=quantity]').val();

        var caseData = {
            id: selectedCase.val(),
            name: selectedCase.data('name'),
            price: parseFloat(selectedCase.data('price'))
        };

        var motherboardData = {
            id: selectedMotherboard.val(),
            name: selectedMotherboard.data('name'),
            price: parseFloat(selectedMotherboard.data('price'))
        };

        var cpuData = {
            id: selectedCpu.val(),
            name: selectedCpu.data('name'),
            price: parseFloat(selectedCpu.data('price'))
        };

        var gpuData = {
            id: selectedGpu.val(),
            name: selectedGpu.data('name'),
            price: parseFloat(selectedGpu.data('price'))
        };

        var memoryData = {
            id: selectedMemory.val(),
            name: selectedMemory.data('name'),
            price: parseFloat(selectedMemory.data('price'))
        };

        var storageData = {
            id: selectedStorage.val(),
            name: selectedStorage.data('name'),
            price: parseFloat(selectedStorage.data('price'))
        };

        var psuData = {
            id: selectedPsu.val(),
            name: selectedPsu.data('name'),
            price: parseFloat(selectedPsu.data('price'))
        };

        var coolingData = {
            id: selectedCooling.val(),
            name: selectedCooling.data('name'),
            price: parseFloat(selectedCooling.data('price'))
        };

        var description = `${caseData.name}|${motherboardData.name}|${cpuData.name}|${gpuData.name}|${memoryData.name}|${storageData.name}|${psuData.name}|${coolingData.name}`;
        var total = (caseData.price + motherboardData.price + cpuData.price + gpuData.price + memoryData.price + storageData.price + psuData.price + coolingData.price).toFixed(2);

        var postData = {
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            image: image,
            name: `Custom Build: ${caseData.name}`,
            description: description,
            quantity: quantity,
            total: total,
            customData: {
                case: caseData,
                motherboard: motherboardData,
                cpu: cpuData,
                gpu: gpuData,
                memory: memoryData,
                storage: storageData,
                psu: psuData,
                cooling: coolingData
            },
        };

        $.ajax({
            // Post data to add_custom_to_basket in basket views.
            type: 'POST',
            url: `/products/add_custom/`,
            data: postData,
            success: function () {
                // redirect to basket on successful post.
                window.location.assign('/basket/');
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});