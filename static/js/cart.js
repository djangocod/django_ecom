$(document).ready(function () {
  $(".add-to-cart").click(function (e) {
    e.preventDefault();
    var prod_id = $(this).closest(".product-data").find(".product-id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "post",
      url: "/carts/add-to-cart/",
      data: {
        product_id: prod_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        document.getElementById("cart-qty").innerHTML = response.cart_qty_total;
      },
    });
  });

  $(".add-to-cart-details").click(function (e) {
    e.preventDefault();
    var prod_id = $(this).closest(".product-data").find(".product-id").val();
    var prod_qty = $(this).closest(".product-data").find(".input-qty").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "post",
      url: "/carts/add-to-cart-detail/",
      data: {
        product_id: prod_id,
        product_qty: prod_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        document.getElementById("cart-qty").innerHTML = response.cart_qty_total;
      },
    });
  });

  var cart_update = $(".update-cart-qty").click(function (e) {
    e.preventDefault();
    var pro_id = $(this).closest(".product-data").find(".product-id").val();
    var pro_qty = $(this)
      .closest(".product-data")
      .find(".update-qty-cart")
      .val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "post",
      url: "/carts/update-cart-qty/",
      data: {
        product_id: pro_id,
        product_qty: pro_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        document.getElementById("cart-qty").innerHTML = response.cart_qty_total;
        location.reload();
        
      },
       
    });
   
  });
      


  $(".remove-cart-item").click(function (e) {
    e.preventDefault();
    var pro_id = $(this).closest(".product-data").find(".product-id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    var pro_index = $(this).closest(".product-data").data("index");
    $.ajax({
      method: "post",
      url: "/carts/delete-cart-qty/",
      data: {
        'product_id': pro_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
        document.getElementById("cart-qty").innerHTML = response.cart_qty_total;
        $('.product-data[data-index="' + pro_index + '"]').remove();
        location.reload();
      },
    });
  });



});
