### future-ish TODOs/open questions

- how to show virtual rc in the iframe? while being signed in? signed in as whom?
  - Jacob is working on it
- make it easy-ish for tv app developers to run this locally i.e. provide instructions
  - even better: not have to run anything. Greg is on it
- deployment to the raspi - can it be semiii automated? one idea from @megaserg that we almost ended up using on the [octopass raspi deployment](https://github.com/gregsadetsky/recurse-rfid-visits/) is to cron fetch from the github repo i.e. the pi auto-checks if there's a new release, picks it up, git pulls, and restarts the service
- also need to create a service so that it auto starts on boot -- see [this](https://github.com/gregsadetsky/recurse-rfid-visits/tree/main/service) again from the octopass hardware, all made by @itay-sho
- to make sure that apps are still running, maybe load it in the iframe... and ping it 5s later / after the dom has loaded i.e. do a "iframe.??.areYouThere()" call and if no response, go to the next app
  - yes, actually do that

### extremely long term/maybe don't do this at all

- interactivity? sound? a webcam that can be turned on a little bit from time to time when folks by the television agree to it, etc.? (only while a button is being held down....??)

### collaborators

- @jryio and @gregsadetsky
- thanks to @nicholasbs for inspiration, support and contributions as well!!
- thanks @will-morningstar for status of pairing stations in Virtual RC idea!
