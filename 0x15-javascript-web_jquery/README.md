<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/uOCIGjC7u4MtYfDwCwODTA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
    <li>Why JQuery make front-end programming so easy (don&rsquo;t forget to tweet today, with the hashtag #ilovejquery :))</li>
    <li>How to select HTML elements in JavaScript</li>
    <li>How to select HTML elements with JQuery</li>
    <li>What are differences between <code>ID</code>, <code>class</code> and <code>tag name</code> selectors</li>
    <li>How to modify an HTML element style</li>
    <li>How to get and update an HTML element content</li>
    <li>How to modify the DOM</li>
    <li>How to make a <code>GET</code> request with JQuery Ajax</li>
    <li>How to make a <code>POST</code> request with JQuery Ajax</li>
    <li>How to listen/bind to DOM events</li>
</ul>
<h2>Tasks</h2>
<p>&nbsp; &nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 0. No JQuery &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that updates the text color of the <code>&lt;header&gt;</code> element to red (<code>#FF0000</code>):</p>
            <ul>
                <li>You must use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You can&rsquo;t use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;0-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>0-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 1. With JQuery &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that updates the text color of the <code>&lt;header&gt;</code>&nbsp; element to red (<code>#FF0000</code>):</p>
            <ul>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;1-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>1-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 2. Click and turn red &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that updates the text color of the &nbsp;<code>&lt;header&gt;</code> element to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p>
            <ul>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;2-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>2-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 3. Add `.red` class &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that adds the class <code>red</code> to the <code>&lt;header&gt;</code> element &nbsp;when the user clicks on the tag <code>DIV#red_header</code></p>
            <ul>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;3-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>3-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 4. Toggle classes &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that toggles the class of the <code>&lt;header&gt;</code> element &nbsp;when the user clicks on the tag <code>DIV#toggle_header</code>:</p>
            <ul>
                <li>The <code>&lt;header&gt;</code> element must always have one class: <code>red</code> or <code>green</code>, never both in the same time and never empty.</li>
                <li>If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.</li>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class=&quot;green&quot;&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;toggle_header&quot;&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;4-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>4-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 5. List of elements &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that adds a <code>&lt;li&gt;</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:</p>
            <ul>
                <li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
                <li>The new element must be added to <code>UL.my_list</code></li>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;add_item&quot;&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class=&quot;my_list&quot;&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;5-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>5-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 6. Change the text &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that updates the text of the <code>&lt;header&gt;</code> element &nbsp;to <code>New Header!!!</code> when the user clicks on <code>DIV#update_header</code></p>
            <ul>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 6-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;update_header&quot;&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;6-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>6-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 7. Star wars character &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that fetches the character <code>name</code> from this URL: <code>https://swapi-api.alx-tools.com/api/people/5/?format=json</code></p>
            <ul>
                <li>The name must be displayed in the HTML tag <code>DIV#character</code></li>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 7-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;character&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;7-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>7-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 8. Star Wars movies &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.alx-tools.com/api/films/?format=json</code></p>
            <ul>
                <li>All movie titles must be list in the HTML tag <code>UL#list_movies</code></li>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 8-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id=&quot;list_movies&quot;&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;8-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>8-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;&nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 9. Say Hello! &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a JavaScript script that fetches from <code>https://hellosalut.stefanbohacek.dev/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML tag <code>DIV#hello</code>.</p>
            <ul>
                <li>The translation of &ldquo;hello&rdquo; must be displayed in the HTML tag <code>DIV#hello</code></li>
                <li>You can&rsquo;t use <code>document.querySelector</code> to select the HTML tag</li>
                <li>You must use the JQuery API</li>
                <li>Your script must work when it is imported from the <code>&lt;head&gt;</code> tag</li>
            </ul>
            <p>Please test with this HTML file in your browser:</p>
            <pre><code>guillaume@ubuntu:~/0x15$ cat 9-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;9-script.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;hello&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x15-javascript-web_jquery</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>9-script.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
            </div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;</p>
<form method="post" action="/projects/305/unlock_optionals"><br></form>
<form method="post" action="/projects/305/unlock_optionals"><br></form>
<p>&nbsp; &nbsp;&nbsp;</p>
<p><br></p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>
<div>
    <div>
        <div>
            <div><br></div>
        </div>
    </div>
</div>
<article>
    <div>
        <div>
            <div><br></div>
        </div>
    </div>
</article>
<p>&nbsp; &nbsp; &nbsp;</p>
<div><br></div>