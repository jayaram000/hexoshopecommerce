$(document).ready(function () {
    
    $('.paywithrazorpay').click(function (e) { 
        e.preventDefault();

        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var zipcode = $("[name='zipcode']").val();
        var city = $("[name='city']").val();
        var country = $("[name='country']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if(phone == "" || address == "" || zipcode == "" || city == "" || country == "")
            {
                
                swal("Alert!","all fields are mandatory","error");
                return false;
            }

        else
            {
                $.ajax({
                    method: "GET",
                    url: "/proceed-to-pay",
                    success: function (response) {
                        // console.log(response)
                        var options = {
                            "key": "rzp_test_1yKhAJQf9lKqyn", // Enter the Key ID generated from the Dashboard
                            "amount": response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                            "currency": "INR",
                            "name": "Hopee",
                            "description": "Thank you for buying from us",
                            "image": "https://example.com/your_logo",
                            // "order_id": "order_IluGWxBm9U8zJ8", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                            
                            "handler": function (responseb){
                                alert(responseb.razorpay_payment_id);
                                    data={
                                    "phone" :phone,
                                    "address" :address,
                                    "zipcode" :zipcode,
                                    "city" :city,
                                    "country" : country,
                                    "payment_method":"online payment",
                                    "payment_id":responseb.razorpay_payment_id,
                                     csrfmiddlewaretoken:token





                                    }

                                $.ajax({
                                    method: "POST",
                                    url: "cart/orderform/",
                                    data: data,

                                    success: function (responsec) {
                                        swal("congratulations",responsec.status,"success");
                                        

                                        
                                    }
                                });
                                
                            },
                            "prefill": {
                                "name": response.user_name,
                                "email": response.user_email,
                                "contact": phone,
                            },
                        
                            "theme": {
                                "color": "#3399cc"
                            }
                        };
                        var rzp1 = new Razorpay(options);
                        rzp1.open();
                        
                    }
                });



                
            };   
        
    });

});




