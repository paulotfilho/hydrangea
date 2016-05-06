### What is Hydrangea?

Hydrangea is a Markdown-powered blog, made with Flask. Just write your .md files in a folder and deploy the app however you want! No database required.

Markdown conversion is made by the [Markdown package], a Python implementation of [John Gruber's Markdown]. It is almost completely compliant with the reference implementation.

Check out some examples:

  - You can have lists
  - they work like
  - magic

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown!

### Version
1.0.0

### Dependencies

Hydrangea has only two dependencies to work properly:

* [Flask] - ```pip install Flask```
* [Markdown] - ```pip install Markdown```

It also uses [Bootstrap], which is loaded directly by their CDN.

   [Markdown package]: <https://pypi.python.org/pypi/Markdown>
   [Markdown]: <https://pypi.python.org/pypi/Markdown>
   [Flask]: <https://pypi.python.org/pypi/Flask>
   [Bootstrap]: <http://getbootstrap.com/>
   [John Gruber's Markdown]: <http://daringfireball.net/projects/markdown/>

