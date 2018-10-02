# SeaGL Tech

## Welcome - How to get help

SeaGL tech is powered by the fine folks reachable at sre@seagl.org and sometimes also, #seagl on FreeNode. They can help with everything below.

## Our Infrastructure

Here's an overview of the SeaGL tech infrastructure.

### Servers

SeaGL uses AWS for core "self-hosted" conference infrastructure.

We use [OSEM](http://osem.io) for event management. The SeaGL OSEM server runs on an EC2 instance. OSEM is a Ruby on Rails app. The backing data store for OSEM is MySQL-ish (Amazon RDS). See a current SeaGL SRE for access.

DNS is handled in Amazon Route 53.

Email from OSEM is routed through gmail via direct SMTP from the system user OSEM runs as.

OSEM is run via [Passenger](https://github.com/phusion/passenger/) on `osem.seagl.org`. Passenger is installed as an [Apache module](https://www.phusionpassenger.com/library/install/apache/install/oss/xenial/). Restart OSEM as root with `systemctl restart apache2`.

### Communication and collaboration tools

Here's a quick list of functions and [3rd party] services used to fulfill them.

* Code: [GitHub](https://github.com/SeaGL/).
* Conference calling: UberConference. Contact staff@seagl.org for call-in information.
* Conference event management system
    * OSEM (Open Source Event Manager). See: [conference website](https://osem.seagl.org), [our fork](https://github.com/SeaGL/osem), [upstream source](https://github.com/openSUSE/osem).
    * See also: [other Free conference event management tools](https://github.com/SeaGL/conference-freedom-tools/blob/master/event_management.md)
* Domain name registrar: Namecheap.
* Email: SeaGL staff use G Suite for `@seagl.org` email accounts.
* Group Chat: [#seagl](https://webchat.freenode.net/?randomnick=1&channels=%23seagl) on [FreeNode](https://freenode.net/kb/answer/chat) ([IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat)).
* Mailing lists: Google Groups.
* Shared calendar: none.
* Shared documents
    * Public: <https://github.com/SeaGL/organization>
    * Private: Google Drive
* www.seagl.org: [GitHub Pages](https://github.com/SeaGL/seagl.github.io).
