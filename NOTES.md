## Develop

XX fast feedback loop

Create another window. In second window, test the site every 10 seconds:

    make watch

In the first window, setup a build-run loop. This command will firstly install new package requirements if any, then start the server. When the server exits, wait 10 seconds, then repeat.

    make loop-minimal

With these two measures in place, we can very rapidly make changes and see the results. When a Developer saves a file, the server restarts, updating itself with the change. Then a few seconds later the automatic test loop shows if the result gets us closer to the goal or not.
