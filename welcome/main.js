window.onload = function() {
	// Initialize the Grid view
	$('.grid').masonry({
        itemSelector: '.grid-item'
    });
	
	$("#loading").fadeOut(315);
	$("body").css("overflow-y", "scroll");
	$("main").animate({opacity: 1}, 636);
};

// Initialize the Popups everywhere
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Translation
function translate(hl) {
    let dict;
    switch (hl) {
        case "fa":
            document.title = "مهدی پرستش";
            $("figcaption").text("مهدی پرستش");
            $("blockquote").html('بنده مدت 7 سال در برنامه نویسی فولستک (بک اند + فرانت اند) و 4 سال در برنامه نویسی اندروید (با زبان های جاوا و کاتلین، بعلاوه فریمورک «فلاتر») تجربه دارم. از ۱۳ سالگی (۱۳۹۲) زبان های جاواسکریپت و PHP را یاد گرفتم. از سال ۱۳۹۷ به برنامه نویسی اندروید مشغول شدم. از سال ۱۳۹۹ نیز به یادگیری سیستم عامل های لینوکسی (خصوصا فدورا، اوبونتو و سنتوس) و یونیکسی (FreeBSD و OpenBSD)، بعلاوه Windows Server و کسب تجربه در آنها مشغول شدم. از سال ۱۴۰۰، الگوریتم های «هوش مصنوعی» را یاد گرفته و تا حدود یک سال مشغول مطالعه و تمرین در این زمینه بودم.');
            $("#cv").text("مشاهده رزومه من");
            $(".instatools .projName").text("اینستاتولز");
            $(".instatools .projDesc").text("آنفالویاب، دانلود هر گونه پست و استوری از اینستاگرام، دانلود پست های سیو شده و استخراج دایرکت ها در HTML ،PDF  و TXT.");
            $(".mergen .projName").text("مِرگِن");
            $(".mergen .projDesc").text("یک نرم افزار هوش مصنوعی منطقی، سیستم عاملی برای یک ربات.");
            $(".telexporter .projName").text("تلکسپورتر");
            $(".telexporter .projDesc").text("اس ام اس ها و تاریخچه تماس های خود را در قالب های وب، پی دی اف و جیسون استخراج کنید.");
            $(".migratio .projName").text("میگراتیو");
            $(".migratio .projDesc").text("یک ابزار جغرافی-آماری برای تعیین کردن بهترین مقصد مهاجرت افراد مختلف.");
            $(".fortuna .projName").text("فورتونا");
            $(".fortuna .projDesc").text("نرم افزاری برای فلسفه «هدونیسم»!");
            $(".friend_tracker .projName").text("ردیاب دوستان");
            $(".friend_tracker .projDesc").text("رفقای خود را از روی نقشه ردیابی نمایید.");
            $(".saam .projName").text("سام");
            $(".saam .projDesc").text("گرداور و ذخیره کننده اطلاعات بورس، ساخته شده بر مبنای متاتریدر 5");
			$("body").css("font-family", "IRANYekan");
			dict = {
			    "Google Play": "گوگل پلی",
			    "Website": "وبسایت",
			    "Android Source": "سورس اندروید",
			    "Flutter Source": "سورس فلاتر",
			    "Software Source": "سورس نرم افزار",
			    "Web Template": "قالب وب",
			    "Server Source": "سورس سرور",
			    "Myket": "مایکت",
			    "Bazaar": "بازار",
			    "Privacy Policy": "سیاست حریم خصوصی",
				
				"Iranian Android Myket Store": "استور ایرانی اندرویدی مایکت",
				"Iranian Android Bazaar Store": "استور ایرانی اندرویدی بازار",
				"Wordpress Theme": "تم وردپرس",
			};
            break;
		default:
		    document.location.assign(document.location + "?hl=en");
			break;
    }
    if (dict) $(".anchor a").each(function() {
		$(this).text(dict[$(this).text()]);
		$(this).attr("data-bs-original-title", dict[$(this).attr("data-bs-original-title")]);
	});
	if (["fa", "ar"].includes(hl))
	    $("blockquote, .projDesc").css("direction", "rtl");
	$('.grid').masonry();
	$("#langSelect").attr("src",$("#lang li img[data-lang="+hl+"]").attr("src"));
}
$("#lang li img").on('click', function(e) { translate($(this).attr("data-lang")); });
if ($("#help").val() != "en") switch ($("#country").val()) {
    case "IR":
        translate("fa");
        break;
}
