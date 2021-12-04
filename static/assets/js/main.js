"use strict";

(function ($) {
  "use strict"; //  Searching & Expand Menu Popup

  var searchToggle = $(".search-toggle"),
    closeA = $(".scale"),
    closeB = $(".searching button"),
    cBody = $("body"),
    closeScale = closeA.add(closeB);

  if (searchToggle.length > 0) {
    searchToggle.on("click", function () {
      cBody.toggleClass("open");
      return false;
    });
  }

  if (closeScale.length > 0) {
    closeScale.on("click", function () {
      cBody.removeClass("open");
      return false;
    });
  }

  $(".close").on("click", function () {
    $("body").removeClass("open");
  }); // AOS.init({
  //   // Global settings:
  //   disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
  //   startEvent: 'DOMContentLoaded', // name of the event dispatched on the document, that AOS should initialize on
  //   initClassName: 'aos-init', // class applied after initialization
  //   animatedClassName: 'aos-animate', // class applied on animation
  //   useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
  //   disableMutationObserver: false, // disables automatic mutations' detections (advanced)
  //   debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
  //   throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)
  //   // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
  //   offset: 120, // offset (in px) from the original trigger point
  //   delay: 0, // values from 0 to 3000, with step 50ms
  //   duration: 400, // values from 0 to 3000, with step 50ms
  //   easing: 'ease-in-out', // default easing for AOS animations
  //   once: true, // whether animation should happen only once - while scrolling down
  //   mirror: false, // whether elements should animate out while scrolling past them
  //   anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
  // });

  /*---------------------------
          Commons Variables
       ------------------------------ */

  var $window = $(window),
    $body = $("body");
  /*--------------------------
      Sticky Menu
    ---------------------------- */

  $($window).on("scroll", function () {
    var scroll = $($window).scrollTop();

    if (scroll < 150) {
      $("#sticky").removeClass("is-isticky");
    } else {
      $("#sticky").addClass("is-isticky");
    }
  });
  /*---------------------------------
            Off Canvas toggler Function
        -----------------------------------*/

  var $offCanvasToggle = $(".offcanvas-toggle"),
    $offCanvas = $(".offcanvas"),
    $offCanvasOverlay = $(".offcanvas-overlay"),
    $mobileMenuToggle = $(".mobile-menu-toggle");
  $offCanvasToggle.on("click", function (e) {
    e.preventDefault();
    var $this = $(this),
      $target = $this.attr("href");
    $body.addClass("offcanvas-open");
    $($target).addClass("offcanvas-open");
    $offCanvasOverlay.fadeIn();

    if ($this.parent().hasClass("mobile-menu-toggle")) {
      $this.addClass("close");
    }
  });
  $(".offcanvas-close, .offcanvas-overlay").on("click", function (e) {
    e.preventDefault();
    $body.removeClass("offcanvas-open");
    $offCanvas.removeClass("offcanvas-open");
    $offCanvasOverlay.fadeOut();
    $mobileMenuToggle.find("a").removeClass("close");
  });
  /*----------------------------------
           Off Canvas Menu
       -----------------------------------*/

  function mobileOffCanvasMenu() {
    var $offCanvasNav = $(".offcanvas-menu, .overlay-menu"),
      $offCanvasNavSubMenu = $offCanvasNav.find(".offcanvas-submenu");
    /*Add Toggle Button With Off Canvas Sub Menu*/

    $offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"></span>');
    /*Category Sub Menu Toggle*/

    $offCanvasNav.on("click", "li a, .menu-expand", function (e) {
      var $this = $(this);

      if ($this.attr("href") === "#" || $this.hasClass("menu-expand")) {
        e.preventDefault();

        if ($this.siblings("ul:visible").length) {
          $this.parent("li").removeClass("active");
          $this.siblings("ul").slideUp();
          $this.parent("li").find("li").removeClass("active");
          $this.parent("li").find("ul:visible").slideUp();
        } else {
          $this.parent("li").addClass("active");
          $this
            .closest("li")
            .siblings("li")
            .removeClass("active")
            .find("li")
            .removeClass("active");
          $this.closest("li").siblings("li").find("ul:visible").slideUp();
          $this.siblings("ul").slideDown();
        }
      }
    });
  }

  mobileOffCanvasMenu();
  var $offcanvasMenu2 = $("#offcanvas-menu2 li a");
  $offcanvasMenu2.on("click", function (e) {
    // e.preventDefault();
    $(this).closest("li").toggleClass("active");
    $(this).closest("li").siblings().removeClass("active");
    $(this).closest("li").siblings().children(".category-sub-menu").slideUp();
    $(this)
      .closest("li")
      .siblings()
      .children(".category-sub-menu")
      .children("li")
      .toggleClass("active");
    $(this)
      .closest("li")
      .siblings()
      .children(".category-sub-menu")
      .children("li")
      .removeClass("active");
    $(this).parent().children(".category-sub-menu").slideToggle();
  });
  /*-----------------------------
        main slider active
      ---------------------------- */

  var $mainSlider = $(".main-slider");
  $mainSlider
    .slick({
      autoplay: true,
      autoplaySpeed: 6000,
      speed: 800,
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      fade: true,
      arrows: true,
      prevArrow:
        '<button class="slick-prev"><i class="fas fa-chevron-left"></i></button>',
      nextArrow:
        '<button class="slick-next"><i class="fas fa-chevron-right"></i></button>',
      responsive: [
        {
          breakpoint: 767,
          settings: {
            dots: true,
            arrows: false,
          },
        },
      ],
    })
    .slickAnimation();
  /*--------------------------
         product slider init
        ---------------------------- */

  var $productSliderInit = $(".product-slider-init");
  $productSliderInit.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: false,
    infinite: false,
    arrows: true,
    speed: 1000,
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1199,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*--------------------------
         popular-slider-init
        ---------------------------- */

  var $popularSlider = $(".popular-slider-init");
  $popularSlider.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: true,
    infinite: false,
    arrows: false,
    speed: 1000,
    slidesToShow: 5,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1280,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 1,
          infinite: false,
          dots: true,
        },
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*--------------------------
        featured-init
  ---------------------------- */

  var $featuredSlider = $(".featured-init");
  $featuredSlider.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: false,
    infinite: false,
    arrows: true,
    speed: 1000,
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1280,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: false,
          dots: false,
        },
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*--------------------------
         product ctry slider init
        ---------------------------- */

  var $productCtry = $(".product-ctry-init");
  $productCtry.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: false,
    infinite: false,
    arrows: true,
    speed: 1000,
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*--------------------------
         blog slider init
        ---------------------------- */

  var $blogInit = $(".blog-init");
  $blogInit.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: false,
    infinite: false,
    arrows: true,
    speed: 1000,
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 575,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*--------------------------
         brand slider init
        ---------------------------- */

  var $brandInit = $(".brand-init");
  $brandInit.slick({
    autoplay: false,
    autoplaySpeed: 10000,
    dots: false,
    infinite: false,
    arrows: true,
    speed: 1000,
    slidesToShow: 6,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-prev"><i class="ion-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="ion-chevron-right"></i></button>',
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 1,
          arrows: true,
          autoplay: true,
        },
      },
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      },
      {
        breakpoint: 575,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          arrows: false,
          autoplay: true,
        },
      }, // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ],
  });
  /*---------------------------
      countdown-syncing
      ---------------------------- */

  $(".countdown-sync-init").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: true,
    draggable: false,
    arrows: false,
    dots: false,
    fade: true,
    asNavFor: ".countdown-sync-nav",
  });
  $(".countdown-sync-nav").slick({
    dots: false,
    arrows: false,
    infinite: true,
    prevArrow:
      '<button class="slick-prev"><i class="fas fa-arrow-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="fas fa-arrow-right"></i></button>',
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: ".countdown-sync-init",
    focusOnSelect: true,
    draggable: false,
  });
  /*---------------------------
      product-syncing
      ---------------------------- */

  $(".product-sync-init").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: true,
    draggable: false,
    arrows: false,
    dots: false,
    fade: true,
    asNavFor: ".product-sync-nav",
  });
  $(".product-sync-nav").slick({
    dots: false,
    arrows: false,
    infinite: true,
    prevArrow:
      '<button class="slick-prev"><i class="fas fa-arrow-left"></i></button>',
    nextArrow:
      '<button class="slick-next"><i class="fas fa-arrow-right"></i></button>',
    slidesToShow: 4,
    slidesToScroll: 1,
    asNavFor: ".product-sync-init",
    focusOnSelect: true,
    draggable: false,
  });
  /*--------------------------
      tooltip
      ---------------------------- */

  $('[data-toggle="tooltip"]').tooltip(); // slider-range

  $("#slider-range").slider({
    range: true,
    min: 0,
    max: 800,
    values: [200, 600],
    slide: function slide(event, ui) {
      $("#amount").val("€" + ui.values[0] + " - €" + ui.values[1]);
    },
  });
  $("#amount").val(
    "€" +
      $("#slider-range").slider("values", 0) +
      " - €" +
      $("#slider-range").slider("values", 1)
  ); // slider-range end

  /*----------------------------------------
      fixed issue in bootstrap tabs problem
      ----------------------------------------- */

  $('a[data-toggle="pill"]').on("shown.bs.tab", function (e) {
    e.target;
    e.relatedTarget;
    $(".slick-slider").slick("setPosition");
  });
  /*-----------------------------------
       fixed issue in bs modal problem
       ---------------------------------- */

  $(".modal").on("shown.bs.modal", function (e) {
    $(".slick-slider").slick("setPosition");
  });
  /*--------------------------
      comment  scroll down 
      ---------------------------- */

  $("#write-comment").on("click", function (e) {
    e.preventDefault();
    $("html, body").animate(
      {
        scrollTop: $(".btn-dark ").offset().top + 750,
      },
      500,
      "linear"
    );
  });
  /*--------------------------     
           counter 
         -------------------------- */

  $(".count").each(function () {
    var count = $(this),
      input = count.find('input[type="number"]'),
      increament = count.find(".increment"),
      decreament = count.find(".decrement"),
      minValue = input.attr("min"),
      maxValue = input.attr("max");
    increament.on("click", function () {
      var oldValue = parseFloat(input.val());

      if (oldValue >= maxValue) {
        var newVal = oldValue;
      } else {
        var newVal = oldValue + 1;
      }

      count.find("input").val(newVal);
      count.find("input").trigger("change");
    });
    decreament.on("click", function () {
      var oldValue = parseFloat(input.val());

      if (oldValue <= minValue) {
        var newVal = oldValue;
      } else {
        var newVal = oldValue - 1;
      }

      count.find("input").val(newVal);
      count.find("input").trigger("change");
    });
  });
  /*-------------------------
    Create an account toggle
    --------------------------*/

  $(".checkout-toggle2").on("click", function () {
    $(".open-toggle2").slideToggle(1000);
  });
  $(".checkout-toggle").on("click", function () {
    $(".open-toggle").slideToggle(1000);
  });
  /*--------------------------
      SscrollUp
    ---------------------------- */
})(jQuery);
