// $(document).ready( function() {
//     $(".sign-in").on("click", function() {
//         $(".modal-body").load("/accounts/login");
//     });
//     $(".sign-up").on("click", function() {
//         $(".modal-body").load("/accounts/signup");
//     });
// });

let signIn = false
//signIn event handler
const signInHandler = function(e){
    if(signIn){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/accounts/login/',
            data:
            {
                username:$("#id_username").val(),
                password:$("#id_password").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(resultData){
                $(".modal-body").html('')
                if(String(resultData).includes('Profile')){
                    window.location.replace("/");
                }else{
                $(".modal-body").html('')
                $(".modal-body").html(resultData)
                    }
                }

            })
    }

}
$(".sign-in").on("click", function() {
    signIn = true;
    $(".modal-body").html('')
    $(".modal-body").load("/accounts/login");
    //start
    //end
});

$('#exampleModal').on('submit','form',signInHandler);


//sign up event handler
const signUpHandler = function(e){
    if(!signIn){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'/accounts/signup/',
            data:
            {
                username:$("#id_username").val(),
                password1:$("#id_password1").val(),
                password2:$("#id_password2").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(resultData){
                if(String(resultData).includes('Profile')){
                    window.location.replace("/");
                }else{
                $(".modal-body").html(resultData)
                }
                }
            })
    }
}
$(".sign-up").on("click", async function() {
    signIn = false;
    $(".modal-body").html('')
    await $(".modal-body").load("/accounts/signup");
});

$('#exampleModal').on('submit','form',signUpHandler);

if(window.location.pathname==='/accounts/login/' || window.location.pathname==='/accounts/signup/'){
window.location.replace("/");
}