var $j = jQuery.noConflict();

var findComments = function(el) {
    var arr = [];
    for(var i = 0; i < el.childNodes.length; i++) {
        var node = el.childNodes[i];
        if(node.nodeType === 8) {
            arr.push(node);
        } else {
            arr.push.apply(arr, findComments(node));
        }
    }
    return arr;
};

var walkDOM = function (node, tag) {
        if(node.nodeName == tag.toUpperCase()){
            return node
        };
        node = node.firstChild;
        while(node) {
            var result = walkDOM(node, tag);
            if (result){
                return result;
            };
            node = node.nextSibling;
        };
};    

var findTargetNode = function(commentNodes, commentStr, tag){
    var target;
    for(i in commentNodes){
        if(commentNodes[i].nodeValue == commentStr){
            node = commentNodes[i].nextSibling;
            while(true){
                var result = walkDOM(node, tag);
                if (result){
                    return result;
                } else {
                    node = node.nextSibling
                };
            };
        };
    };
    return null;
};

var addAttrs = function(target, attrs){
    $target = $j(target);
    for(k in attrs){
        if(k == 'class'){
            var origin = $target.attr('class');
            $target.attr('class', origin + ' ' + attrs[k]);
        }else{
            $target.attr(k, attrs[k]);
        };
    };
};

$j(document).ready(function() {
    var commentNodes = findComments(document);
    
    // Add Attr to tag

    
        var img7b6ffa5ebb5690d71f70a35f5218b520 = findTargetNode(commentNodes, 'CMS:index-span-1', 'img');
        if(img7b6ffa5ebb5690d71f70a35f5218b520 != null){  
            var attrs7b6ffa5ebb5690d71f70a35f5218b520 = {
                
                    'alt': ''
                
            };
            addAttrs(img7b6ffa5ebb5690d71f70a35f5218b520, attrs7b6ffa5ebb5690d71f70a35f5218b520)
        };
    
        var a266ef1e65530af84ab3062eb20ea92fa = findTargetNode(commentNodes, 'CMS:index-a-22', 'a');
        if(a266ef1e65530af84ab3062eb20ea92fa != null){  
            var attrs266ef1e65530af84ab3062eb20ea92fa = {
                
            };
            addAttrs(a266ef1e65530af84ab3062eb20ea92fa, attrs266ef1e65530af84ab3062eb20ea92fa)
        };
    
        var img266ef1e65530af84ab3062eb20ea92fa = findTargetNode(commentNodes, 'CMS:index-a-22', 'img');
        if(img266ef1e65530af84ab3062eb20ea92fa != null){  
            var attrs266ef1e65530af84ab3062eb20ea92fa = {
                
                    'alt': '',
                
                    'class': 'img-responsive'
                
            };
            addAttrs(img266ef1e65530af84ab3062eb20ea92fa, attrs266ef1e65530af84ab3062eb20ea92fa)
        };
    
        var a681177a526c99e9d9778a5498943438b = findTargetNode(commentNodes, 'CMS:index-a-24', 'a');
        if(a681177a526c99e9d9778a5498943438b != null){  
            var attrs681177a526c99e9d9778a5498943438b = {
                
            };
            addAttrs(a681177a526c99e9d9778a5498943438b, attrs681177a526c99e9d9778a5498943438b)
        };
    
        var img681177a526c99e9d9778a5498943438b = findTargetNode(commentNodes, 'CMS:index-a-24', 'img');
        if(img681177a526c99e9d9778a5498943438b != null){  
            var attrs681177a526c99e9d9778a5498943438b = {
                
                    'alt': '',
                
                    'class': 'img-responsive'
                
            };
            addAttrs(img681177a526c99e9d9778a5498943438b, attrs681177a526c99e9d9778a5498943438b)
        };
    
        var a4757812fe5ec39f85a270259c663c9ec = findTargetNode(commentNodes, 'CMS:index-a-26', 'a');
        if(a4757812fe5ec39f85a270259c663c9ec != null){  
            var attrs4757812fe5ec39f85a270259c663c9ec = {
                
            };
            addAttrs(a4757812fe5ec39f85a270259c663c9ec, attrs4757812fe5ec39f85a270259c663c9ec)
        };
    
        var img4757812fe5ec39f85a270259c663c9ec = findTargetNode(commentNodes, 'CMS:index-a-26', 'img');
        if(img4757812fe5ec39f85a270259c663c9ec != null){  
            var attrs4757812fe5ec39f85a270259c663c9ec = {
                
                    'alt': '',
                
                    'class': 'img-responsive'
                
            };
            addAttrs(img4757812fe5ec39f85a270259c663c9ec, attrs4757812fe5ec39f85a270259c663c9ec)
        };
    
        var a8da6f1783d563749b367066339a946ad = findTargetNode(commentNodes, 'CMS:index-a-35', 'a');
        if(a8da6f1783d563749b367066339a946ad != null){  
            var attrs8da6f1783d563749b367066339a946ad = {
                
                    'class': 'scroll'
                
            };
            addAttrs(a8da6f1783d563749b367066339a946ad, attrs8da6f1783d563749b367066339a946ad)
        };
    
        var img8da6f1783d563749b367066339a946ad = findTargetNode(commentNodes, 'CMS:index-a-35', 'img');
        if(img8da6f1783d563749b367066339a946ad != null){  
            var attrs8da6f1783d563749b367066339a946ad = {
                
                    'alt': ''
                
            };
            addAttrs(img8da6f1783d563749b367066339a946ad, attrs8da6f1783d563749b367066339a946ad)
        };
    
});