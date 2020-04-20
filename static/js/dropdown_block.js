$(function() {
    $("div[id*='block-']").hide(); 
    });
    
function toggle(objName) {
    var obj = $(objName),
    blocks = $("div[id*='block-']");
    
    if (obj.css("display") != "none") {
    obj.animate({ height: 'hide' }, 500);
    } else {
    var visibleBlocks = $("div[id*='block-']:visible");
    
    if (visibleBlocks.length < 1) {
    obj.animate({ height: 'show' }, 500);
    } else {
    $(visibleBlocks).animate({ height: 'hide' }, 500, function() {
    obj.animate({ height: 'show' }, 500);
    }); 
    }
    }
};
