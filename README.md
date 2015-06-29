[Example]:http://eldrad.cs-i.brandeis.edu:8080/python-as-web-service-shi-2013-12-17.html

# Why HtMant?
Generally we could log our steps into wiki. 
But sometime, we want to keep log locally. 
When such time, html could be a good template for these:

1. Outline link
2. Sections
3. Figure
4. Table

High available, and editable. 

Here is an [Example](https://rawgit.com/chunqishi/htmant/master/template-shi-2013-11-15.html).

# Usage

## Navigating Bar

Define <nav> with class "nav-bar"
```
    <nav class="nav-bar">
        <a href="#available-services">available services</a>
        | 
        <a href="#">wrap web service</a>
        |
        <a href="#">deploy</a></nav>


```

Add H2 as section, and name for navigating bar

```
	<a name="available-services" />
	<h2>Available Service <a href="#_top_" style="text-decoration: none;">^</a></h2>
```

## Section

Use class "reset" to recalculate subsection number
```
<h2>Available Service <a href="#_top_" style="text-decoration: none;">^</a></h2>

<h3 class="reset"> Main Available Services</h3>

```

## Code and Sample

Define codes.
```
<code class="code prettyprint linenums">//
String x = "good."
String y = "morning.".
</code>
```


Define samples.
```
<samp class="sample">[shicq@chilote lapps]$ git --version <span style="color:blue">&crarr;</span>
</samp>  
```

## Table

Three types of tables styles are defined: class "g" (Grid), "h" (Horizontal) "v" (Vertical)
```
<table class="g">
<thead><tr>
<th>name</th>
<th>age</th>
<th>sex</th></tr>
</thead>
<tbody>
<tr>
<td> joan </td>
<td> 24 </td>
<td> f </td>
</tr>
<tr>
<td> archie </td>
<td> 29 </td>
<td> m </td>
</tr>
<tr>
<td> bella </td>
<td> 45 </td>
<td> f </td>
</tr>
</tbody>
</table>
```

## Embedded Image

Python tool imgtobase64.py could generate embeded base64 <img> data for images under current directory (.) 

With img data, you can add figures

```
<figure>
    <img src="data:image/jpeg;base64,------" alt="" />
    <figcaption><h4> A view of the pulpit rock in Norway.</h4></figcaption></figure>

```



## TODO
