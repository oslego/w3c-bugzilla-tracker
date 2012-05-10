W3C BugzillaTracker
=====

W3C BugzillaTracker makes it easier for editors to keep track of bugs opened for their proposals. The script handles synchronizing bugs between the W3C Bugzilla instance and the bug data embedded into the W3C documents. 

A bug dashboard is layered on top of the W3C spec with notable bug changes: new, updated or resolved.

Usage
-----       

1 Include the required files 
<pre>
    &lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;style/issues.css&quot;&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;scripts/BugzillaTrackerUtil.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;scripts/BugzillaTracker.js&quot;&gt;&lt;/script&gt;  
</pre>
  

2 Add the bug template to the document
<pre>
&lt;script type=&quot;text/template&quot; id=&quot;issue-template&quot;&gt;
    &lt;div class=&quot;issue-marker&quot; data-bug_id=&quot;{{bug_id}}&quot; data-bug_status=&quot;{{bug_status}}&quot;&gt;
    &lt;a href=&quot;https://www.w3.org/Bugs/Public/show_bug.cgi?id={{bug_id}}&quot;&gt;Bug-{{bug_id}}&lt;/a&gt;
    &lt;div class=&quot;issue-details&quot;&gt;
        &lt;p class=&quot;short-desc&quot;&gt;{{short_desc}}&lt;/p&gt;
    &lt;/div&gt;  
    &lt;/div&gt;
&lt;/script&gt; 
</pre> 
           

**Important**   
The bugs hardcoded in the document need to follow the same template.
       

3 Call the script with the desired product and component

<pre>
&lt;script type=&quot;text/javascript&quot;&gt;
    // product = &quot;CSS&quot;
    // component = &quot;Regions&quot;
    checkSpecificationIssues(&#x27;CSS&#x27;, &#x27;Regions&#x27;);        
&lt;/script&gt;    
</pre>


Browser requirements
-----
The script is expected to work in Google Chrome, Safari, Firefox, Opera and Internet Explorer 9+

