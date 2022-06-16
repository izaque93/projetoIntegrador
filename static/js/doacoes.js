console.log("Entrouuuu")

$(document).ready(function() {

    $(".plus_roupas").click(function() {
        a = $(".num_roupas")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_roupas").text(a)
    })

    $(".min_roupas").click(function() {
        a = $(".num_roupas")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_roupas").text(a)
        }
    })

    $(".plus_objetos").click(function() {
        a = $(".num_objetos")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_objetos").text(a)
    })

    $(".min_objetos").click(function() {
        a = $(".num_objetos")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_objetos").text(a)
        }
    })

    $(".plus_calcados").click(function() {
        a = $(".num_calcados")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_calcados").text(a)
    })

    $(".min_calcados").click(function() {
        a = $(".num_calcados")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_calcados").text(a)
        }
    })

    $(".plus_brinquedos").click(function() {
        a = $(".num_brinquedos")[0].outerText
        a++
        a = (a < 10) ? "0" + a : a;
        $(".num_brinquedos").text(a)
    })

    $(".min_brinquedos").click(function() {
        a = $(".num_brinquedos")[0].outerText
        if (a > 1) {
            a--
            a = (a < 10) ? "0" + a : a;
            $(".num_brinquedos").text(a)
        }
    })

    $("#enviar_doacoes").click(function() {

        roupas = $("#roupas").text()
        num_roupas = $(".num_roupas").text()
        objetos = $("#objetos").text()
        num_objetos = $(".num_objetos").text()
        calcados = $("#calcados").text()
        num_calcados = $(".num_calcados").text()
        brinquedos = $("#brinquedos").text()
        num_brinquedos = $(".num_brinquedos").text()
        console.log(roupas, num_roupas, objetos, num_objetos, calcados, num_calcados, brinquedos, num_brinquedos)

        dados = {
            roupas,
            num_roupas,
            objetos,
            num_objetos,
            calcados,
            num_calcados,
            brinquedos,
            num_brinquedos
        }

        $.ajax({
            url: "/enviaDadosDoacoes",
            type: "GET",
            dataType: "json",
            data: dados,
            success: function(response) {
                console.log(response)
                    //data - response from server
            },
            error: function(response) {

            }
        });

        console.log(dados)



    })

    $("#enviarCadastro").click(function() {

        email = $("#email").val()
        password = $("#password").val()
        confpassword = $("#confpassword").val()

        console.log(email,password, confpassword)

        dados = {
            email,
            password,
            confpassword
        }

        // $.ajax({
        //     url: "/enviaDadosDoacoes",
        //     type: "GET",
        //     dataType: "json",
        //     data: dados,
        //     success: function(response) {
        //         console.log(response)
        //             //data - response from server
        //     },
        //     error: function(response) {

        //     }
        // });

        console.log(dados)



    })

    $("#enviar").click(function(){
        message = $("#message").val()
        name = $("#name").val()
        email = $("#email").val()
        subject = $("#subject").val()

        dados = {message, name, email, subject}

        console.log("Entrouu", dados)
        
        $.ajax({
            url: "/enviarEmailContatos",
            type: "GET",
            dataType: "json",
            data: dados,
            success: function(response) {
                console.log(response)
                    //data - response from server
            },
            error: function(response) {

            }
        });

    })
})


/*const plus_roupas = document.querySelector(".plus")
const minus_roupas = document.querySelector(".minus")
const num_roupas = document.querySelector(".num");
let a = 1;
plus_roupas.addEventListener("click", () => {
    a++;
    a = (a < 10) ? "0" + a : a;
    num_roupas.innerText = a;
});

minus_roupas.addEventListener("click", () => {
    if (a > 1) {
        a--;
        a = (a < 10) ? "0" + a : a;
        num_roupas.innerText = a;
    }
});*/