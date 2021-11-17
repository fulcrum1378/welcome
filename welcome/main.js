// Initialize the Grid view
$('.grid').masonry({
    itemSelector: '.grid-item'
});

// Initialize the Popups everywhere
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Translation
var params = {}, rawParams = window.location.search.split("&");
rawParams.forEach(function (p) {
    let v = p.split("="), key = v[0];
    if (key.charAt(0) == "?") key = key.substring(1);
    params[key] = decodeURIComponent(v[1]);
});
function translate(hl) {
    switch (hl) {
        case "fa":
            document.title = "مهدی پرستش";
            $("p.mahdi").text("مهدی پرستش");
            $("blockquote.mahdi").html('بنده مدت 6 سال در برنامه نویسی فولستک (بک اند + فرانت اند) و 3 سال در برنامه نویسی اندروید (با زبان های جاوا و کاتلین، بعلاوه فریمورک «فلاتر») تجربه دارم. از سال 1399 نیز به یادگیری سیستم عامل های لینوکسی (خصوصا فدورا، اوبونتو و سنتوس) و یونیکسی (FreeBSD و OpenBSD)، بعلاوه Windows Server و کسب تجربه در آنها مشغول شدم و در سیستم عامل جدید الورود شرکت هواوی (HarmonyOS) نیز کمی مهارت دارم. از سال 1400، الگوریتم های «هوش مصنوعی» را یاد گرفته و هم اکنون مشغول مطالعه و تمرین در این زمینه هستم.');
            $("#cv").text("مشاهده رزومه من");
            $(".mergen:eq(1) .projName").text("مِرگِن");
            $(".mergen:eq(1) .projDesc").text("یک نرم افزار هوش مصنوعی منطقی، سیستم عاملی برای یک ربات.");
            $(".mergen:eq(2) .projName").text("آوابات");
            $(".mergen:eq(2) .projDesc").text("ابزار های تشخیص گفتار، تبدیل متن به گفتار و تشخیص متن از روی عکس برای زبان های فارسی و ترکی");
            $(".telexporter .projName").text("تلکسپورتر");
            $(".telexporter .projDesc").text("اس ام اس ها و تاریخچه تماس های خود را در قالب های وب، پی دی اف و جیسون استخراج کنید.");
            $(".migratio:eq(1) .projName").text("میگراتیو");
            $(".migratio:eq(1) .projDesc").text("وبسایت وردپرسی میگراتیو");
            $(".migratio:eq(2) .projName").text("میگراتیو (اندروید)");
            $(".migratio:eq(2) .projDesc").text("یک ابزار جغرافی-آماری برای تعیین کردن بهترین مقصد مهاجرت افراد مختلف.");
            $(".sexbook .projName").text("سکسبوک");
            $(".sexbook .projDesc").text("زندگی جنسی خود را به آسانی کنترل کنید.");
            $(".friend_tracker .projName").text("ردیاب رفقا");
            $(".friend_tracker .projDesc").text("رفقای خود را از روی نقشه ردیابی نمایید.");
            $(".saam .projName").text("سام");
            $(".saam .projDesc").text("گرداور و ذخیره کننده اطلاعات بورس، ساخته شده بر مبنای متاتریدر 5");
            break;
    }
}
if (params.hasOwnProperty("hl")) translate(params["hl"])
