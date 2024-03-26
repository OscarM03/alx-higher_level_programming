<div>
    <div>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to <a href="https://intranet.alxswe.com/rltoken/yZIL5HK-2hHAP-RJF6yInQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>Why JavaScript programming is amazing</li>
            <li>How to manipulate JSON data</li>
            <li>How to use <code>request</code> and fetch API</li>
            <li>How to read and write a file using <code>fs</code> module</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.&nbsp;</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
            <li>All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 14.x)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
            <li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should be <code>semistandard</code> compliant. <a href="https://intranet.alxswe.com/rltoken/W9rASrTqkF-xXjcwomrMLw" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="https://intranet.alxswe.com/rltoken/NZR55f9vk1dZXj5q7UI5mQ" title="AirBnB style" target="_blank">AirBnB style</a></li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using <code>wc</code></li>
            <li>You are not allowed to use <code>var</code></li>
        </ul>
        <h2>More Info</h2>
        <h3>Install Node 14</h3>
        <pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>
        <h3>Install semi-standard</h3>
        <p><a href="https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="Documentation" target="_blank">Documentation</a></p>
        <pre><code>$ sudo npm install semistandard --global
</code></pre>
        <h3>Install <code>request</code> module and use it</h3>
        <p><a href="https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ" title="Documentation" target="_blank">Documentation</a></p>
        <pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>
        <p><strong>Notes:</strong> Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it&rsquo;s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).</p>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>
<h2>Tasks</h2>
<p>&nbsp; &nbsp;</p>
<div>
    <div>&nbsp; &nbsp;<div>
            <h3>&nbsp; &nbsp; &nbsp; 0. Readme &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that reads and prints the content of a file.</p>
            <ul>
                <li>The first argument is the file path</li>
                <li>The content of the file must be read in <code>utf-8</code></li>
                <li>If an error occurred during the reading, print the error object</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open &apos;doesntexist&apos;
    at Error (native)
  errno: -2,
  code: &apos;ENOENT&apos;,
  syscall: &apos;open&apos;,
  path: &apos;doesntexist&apos; }
guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>0-readme.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 1. Write me &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that writes a string to a file.</p>
            <ul>
                <li>The first argument is the file path</li>
                <li>The second argument is the string to write</li>
                <li>The content of the file must be written in <code>utf-8</code></li>
                <li>If an error occurred during while writing, print the error object</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt &quot;Python is cool&quot;
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo &quot;&quot;
Python is cool
guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>1-writeme.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 2. Status code &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that display the status code of a <code>GET</code> request.</p>
            <ul>
                <li>The first argument is the URL to request (<code>GET</code>)</li>
                <li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
                <li>You must use the module <code>request</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>2-statuscode.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 3. Star wars movie title &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>
            <ul>
                <li>The first argument is the movie ID</li>
                <li>You must use the <a href="https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a> with the endpoint <code>https://swapi-api.alx-tools.com/api/films/:id</code></li>
                <li>You must use the module <code>request</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>3-starwars_title.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 4. Star wars Wedge Antilles &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that prints the number of movies where the character &ldquo;Wedge Antilles&rdquo; is present.</p>
            <ul>
                <li>The first argument is the API URL of the <a href="https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a>: <code>https://swapi-api.alx-tools.com/api/films/</code></li>
                <li>Wedge Antilles is character ID <code>18</code> - your script <strong>must</strong> use this ID for filtering the result of the API</li>
                <li>You must use the module <code>request</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>4-starwars_count.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 5. Loripsum &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that gets the contents of a webpage and stores it in a file.</p>
            <ul>
                <li>The first argument is the URL to request</li>
                <li>The second argument the file path to store the body response</li>
                <li>The file must be UTF-8 encoded</li>
                <li>You must use the module <code>request</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
&lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. &lt;/p&gt;

&lt;p&gt;Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. &lt;/p&gt;

&lt;p&gt;Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. &lt;/p&gt;

&lt;p&gt;Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. &lt;/p&gt;

guillaume@ubuntu:~/0x14$ 
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>5-request_store.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
            <h3>&nbsp; &nbsp; &nbsp; 6. How many completed? &nbsp; &nbsp;</h3>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mandatory &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
        </div>&nbsp;<div>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<p>Write a script that computes the number of tasks completed by user id.</p>
            <ul>
                <li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
                <li>Only print users with completed task</li>
                <li>You must use the module <code>request</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ &apos;1&apos;: 11,
  &apos;2&apos;: 8,
  &apos;3&apos;: 7,
  &apos;4&apos;: 6,
  &apos;5&apos;: 12,
  &apos;6&apos;: 6,
  &apos;7&apos;: 9,
  &apos;8&apos;: 11,
  &apos;9&apos;: 8,
  &apos;10&apos;: 12 }
guillaume@ubuntu:~/0x14$
</code></pre>
        </div>&nbsp;<div>
            <div>
                <p><strong>Repo:</strong></p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<ul>
                    <li>GitHub repository: <code>alx-higher_level_programming</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>Directory: <code>0x14-javascript-web_scraping</code></li>
                    <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
                    <li>File: <code>6-completed_tasks.js</code></li>
                </ul>
            </div>
        </div>&nbsp; &nbsp;<div>
            <div>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</div>
        </div>
    </div>
</div>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
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
<form method="post" action="/projects/333/unlock_optionals"><br></form>
<article>
    <div>
        <div>
            <div>
                <div>
                    <form method="post" action="/projects/333/unlock_optionals"><br></form>&nbsp; &nbsp;&nbsp;<p><br></p>
                </div>
            </div>
        </div>
    </div>
</article>
<p>&nbsp; &nbsp; &nbsp;</p>
<div><br></div>