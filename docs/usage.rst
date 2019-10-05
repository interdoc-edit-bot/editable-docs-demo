=====
Usage
=====

Edit this page by clicking on the text and then see your pull request `on
GitHub <https://github.com/orange-aardvark/editable-docs-demo/pulls>`__.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc
aliquet bipbendum enim. In massa tempor nec feugiat. Nunc aliquet bibendum enim
facilisis gravida. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper.
Amet luctus venenatis lectus magna fringilla. Volutpat maecenas volutpat
blandit aliquam etiam erat velit scelerisque in. Egestas egestas fringilla
phasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus
semper eget duis. Nulla pharetra diam sit amet nisl suscipit. Sed adipiscing
diam donec adipiscing tristique risus nec feugiat in. Fusce ut placerat orci
nulla. Pharetra vel turpis nunc eget lorem dolor. Tristique senectus et netus
et malesuada.

Etiam tempor orci eu lobortis elementum nibh tellus molestie. Neque egestas
congue quisque egestas. Egestas integer eget aliquet nibh praesent tristique.
Vulputate mi sit amet mauris. Sodales neque sodales ut etiam sit. Dignissim
suspendisse in est ante in. Volutpat commodo sed egestas egestas. Felis donec
et odio pellentesque diam. Pharetra vel turpis nunc eget lorem dolor sed
viverra. Porta nibh venenatis cras sed felis eget. Aliquam ultrices sagittis
orci a. Dignissim diam quis enim lobortis. Aliquet porttitor lacus luctus
accumsan. Dignissim convallis aenean et tortor at risus viverra adipiscing at.



.. raw:: html

    <script src="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/js/medium-editor.min.js"></script>

    <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/medium-editor@latest/dist/css/medium-editor.min.css" type="text/css" media="screen" charset="utf-8">

    <script>
    var editor = new MediumEditor('body p');


     editor.subscribe('focus', function(data, editable) { if (!editable.hasAttribute('data-original')) {
     editable.dataset.original = editable.innerText};
                                                        });

     editor.subscribe('blur', function(data, editable) {
     old_html = editable.dataset.original;
     new_html = editable.innerHTML;
     if (old_html == new_html) {
         return;
     }
     index = editable.dataset.mediumEditorEditorIndex;
     var xhr = new XMLHttpRequest();
     xhr.open("POST", 'https://cors-anywhere.herokuapp.com/https://sleepy-harbor-00552.herokuapp.com/', true);
     xhr.setRequestHeader('Content-Type', 'application/json');
     data = {
         index: index,
         old_html: old_html,
         new_html: new_html,
         rendered_html_url: document.URL,
         rendered_rst_url: document.evaluate('//a[@class="fa fa-github"]', document, null, XPathResult.ANY_TYPE, null).iterateNext().href
    };
    xhr.send(JSON.stringify(data))});

    </script>
