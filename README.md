# Script to quickly display IPs, ports and hostnames through Shodan

This script can be used to add a library of keywords and you do a quick search in shodan, and go deep from there.

Obviously it is recommended to modify the dorks to preference, make use of a list or to search manually.

![alt text](image-2.png)

## Output example
![alt text](image-1.png)

hello <a href="www.google.com">*you*</a>
[some text](javascript:alert('xss'))
> hello <a name="n"
> href="javascript:alert('xss')">*you*</a>
<blockquote>
 <p>hello <a name="n"
 href="javascript:alert('xss')"><em>you</em></a></p>
</blockquote>
%3Ca+href%3D%22%01java%03script%3Aconfirm%28document.domain%29%22%3EClick+to+execute%3Ca%3E%0D%0A
[Click Me](https://www.example.com/)
![The goodest boy](https://images.unsplash.com/the_good_boy.png)
![Uh oh...]("onerror="alert('XSS'))
