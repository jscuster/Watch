# The Watch Script #

### by [Jason Custer](mailto://jscuster@gmail.com) ###

	This script watches a director (folder if you prefer) for changes to files of a specified type, then runs the specified command on those files.

	For example, suppose you're working on a project in c. Every time you update any c file in a particular directory, you want to compile it. Try this.

		watch . gcc c

	This calls watch, tells it to watch the current directory (.), and to run "gcc" on any files with the .c extension.

	Ok, let's get more complex. Suppose you want to execute a script on a filetype (file with a particular extension) whenever a file is changed or modified. Let's also say you want to pass commands to that script.

		watch . "myscript -a1 -a2 -a3 %f -a4" typ

	This tells watch to watch the current folder and run the command in quotes, substituting %f for the filename. 

	When ever watch sees a change or addition to the files in the folder you choose, it runs the command and copys the output to [filename]_results.txt.

### Practical application ###

Suppose you are working on a project. You can't take your computer with you, but you do have your phone. Here's what you can do.

1. Copy the project to Dropbox or the like.
2. "watch" the project folder and run either the compilation command, or a script.
3. Change and add files as you wish.
4. Read [filename]-results.txt to see the result of the compile/script.

### Why is this here? ###

	I created this script because IOS doesn't allow compilation. I wanted to write code, check the results, and do it all from my IOS device, while away from my computer.

### Thanks ###

I hope you enjoy this code as much as me.

Jason Custer
