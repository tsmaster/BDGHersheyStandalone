Hershey Font Renderer [Standalone Repo]
====================

By Dave LeCompte

This is a small bit of Python3 code that draws text with Hershey
Fonts. I implemented this based on the description at unpythonic.net
(see link, below), which describes the JHF file format. I make no
warrantees about its usefulness, suitability, or safety of this code -
you're on your own.

Indeed, the code as provided here has several dependencies, including
drawSvg, as this is intended to draw directly to SVGs, but it can be
adapted to other vector drawing contexts, like driving an AxiDraw or
EggBot directly using the EMS Python API.

Another dependency that this code has that is not included here is my
Big Dice Games Math library (bdgmath). Looking at the code as I write
this, this is only used to provide a 2d vector class - perhaps a
Python tuple would suffice?

No support is offered for this, but if you find some glaring flaw in
it, I'll certainly consider fixes.

I feel like this is an unusually blunt README. My intention is to
bundle a (later?) version of this in with the rest of my code at the
end of Genuary 2021 (January), and maybe that will be a better version
for future developers.

This software is provided under MIT license. For details see
license.txt in this same directory.


Links
====================
https://en.wikipedia.org/wiki/Hershey_fonts
https://emergent.unpythonic.net/software/hershey
https://wiki.evilmadscientist.com/Hershey_Text

