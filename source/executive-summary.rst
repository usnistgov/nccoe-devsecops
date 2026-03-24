DevSecOps Practices
====================



.. rst-class:: frontmatter-header
**DISCLAIMER**

Certain commercial entities, equipment, products, or materials may be identified by name or company logo or other insignia in order to acknowledge their
participation in this collaboration or to describe an experimental procedure or concept adequately. Such identification is not intended to imply special status
or relationship with NIST or recommendation or endorsement by NIST or NCCoE; neither is it intended to imply that the entities, equipment, products, or
materials are necessarily the best available for the purpose.


.. rst-class:: frontmatter-header
**FEEDBACK**

You can view or download the document at the `NCCoE Secure Software Development, Security, and Operations (DevSecOps) Practices project page <https://www.nccoe.nist.gov/projects/secure-software-development-security-and-operations-devsecops-practices>`__.

NIST will use an agile process to make updates available as the project continues. We are asking for feedback on this document.

Comments on this publication may be submitted to: nccoe-devsecops@list.nist.gov

Public comment period: March 24, 2026, through April 24, 2026.

All comments are subject to release under the Freedom of Information Act.

NIST is particularly interested in your feedback on the following questions:

1. How do you expect this document to influence your future practices and processes? What guidelines would be most helpful to meet your expectations?

2. How do you envision using this document? What changes would you like to see to increase/improve that use?

3. What suggestions do you have on changing the format of the provided information?


.. rst-class:: centered

| National Cybersecurity Center of Excellence
| National Institute of Standards and Technology
| 100 Bureau Drive
| Mailstop 2002
| Gaithersburg, MD 20899
| Email: nccoe@nist.gov


.. rst-class:: frontmatter-header
**NATIONAL CYBERSECURITY CENTER OF EXCELLENCE**

The National Cybersecurity Center of Excellence (NCCoE), a part of the National Institute of Standards and Technology (NIST), is a collaborative hub where
industry organizations, government agencies, and academic institutions work together to address businesses’ most pressing cybersecurity issues. This
public-private partnership enables the creation of practical cybersecurity solutions for specific industries, as well as for broad, cross-sector technology
challenges. Through consortia under Cooperative Research and Development Agreements (CRADAs), including technology partners—from Fortune 50 market leaders to
smaller companies specializing in information technology security—the NCCoE applies standards and best practices to develop modular, adaptable example
cybersecurity solutions using commercially available technology. The NCCoE documents these example solutions in the NIST Special Publication (SP) 1800 series,
which maps capabilities to the NIST Cybersecurity Framework and details the steps needed for another entity to re-create the example solution. The NCCoE was
established in 2012 by NIST in partnership with the State of Maryland and Montgomery County, Maryland.

| To learn more about the NCCoE, visit https://www.nccoe.nist.gov/. To learn more about NIST, visit
| `https://www.nist.gov <https://www.nist.gov/>`__\ *.*

.. rst-class:: frontmatter-header
**ABSTRACT**

Today's software applications are typically constructed by combining a diverse range of elements, including components, frameworks, libraries, and tools. Rather than building everything from the ground up, developers often leverage a mix of internally developed and externally sourced components. This modular development approach, coupled with Development Operations (DevOps) practices that integrate development and operations teams, enables a modern software development process that delivers improved quality, reliability, agility, and efficiency, while also fostering collaboration among various teams. The adoption of Development, Security, and Operations (DevSecOps), a methodology that builds on the DevOps philosophy and integrates security into every phase of software development, is further accelerating this trend. Additionally, the utilization of cloud-native technologies and AI is enhancing security and optimizing efficiency. However, the complexities and rapid pace of modern software development can still introduce security risks, highlighting the need for continuous security monitoring and improvement. To address this challenge, the NCCoE is undertaking a project that demonstrates and documents risk-based approaches and recommendations for DevSecOps practices aligned with the `NIST Secure Software Development Framework (SSDF) <https://doi.org/10.6028/NIST.SP.800-218>`__. This project showcases secure software development by implementing example processes that adhere to the SSDF's recommended practices.


.. rst-class:: frontmatter-header
**KEYWORDS**

*DevOps; DevSecOps;* *Secure software development; Secure Software Development Framework (SSDF).*

.. rst-class:: frontmatter-header
**ACKNOWLEDGMENTS**

We are grateful to the following individuals for their generous contributions of expertise and time.

-  AMI: Veerajothi Ramasamy

-  Black Duck: Al Bessey, Rod Musser, Brendon Rizzolo, Rick Smith

-  CyberArk: David Dennenberg, Joshua Freeman, Oana Garnett, Steve Judd, Darren Khan, Evan Litwak, Grayson Miller, Gram Slingbam, Bryan Sowell, Riaz
   Vellamparambil, Ivan Wallis, Nathan Whipple

-  Endor Labs: Andrew Davidson, Ron Harnik, Karl Mattson, Shruti Sundaresh

-  Dell Technologies: Mukund Khatri, Sean Schwoerer, Sam Sehgal

-  DigiCert: Corey Bonnell, Don Brooks, Mohan Dattatreya, Tim Hollebeek, Sam Merrill, Anshuman Mor, Michael Rudloff, Bob Vogt, Taylor Williams

-  GitLab: Sameer Kamani, Joel Krooswyk\*

-  Google: Bob Callaway, Chris Cornillie, Wendy Dembowski, Kim Gajewski, Tom Hennen, Shmuel Herzberg, Al Huizenga, Dustin Ingram, Stephanie Kiel, Leah Rivers

-  IBM: Anamika Agrawal, Pradeep Balachandran, Jen Gilbert, Piyush Mundra, Smith Naik, Nic Sauriol, Ritchie Schacher

-  Microsoft: Andrew Brenner, Nick Couraud, Leonard Dattilo, Adrian Diglio, Pedro Enriquez, Lara Goldstein, Dick Lake, Toddy Mladenov, Tony Rice, Zachary Steindler, Betty Tso,
   Michael Yomokoh, Yi Zha

-  MITRE: Jonathan Davis, John Kent, Lauren Swan, Theresa Suloway, Thomas Walters

-  NextLabs: Tony Berning, Julius Brosas, Johnwin Johnrose, Ting Ning, Harvey Shan, Emmanuel Thioux, Allen Yuen

-  NIST: Cherilyn Pascoe, Kevin Stine

-  Palo Alto Networks: David Kubicki, Sean Morgan\*, Alfredo Motta, Eden Tesfay\*, Norman Wong, Jeff Yuetter

-  Sagittal: Sam Lacey

-  Scribe Security: Rubi Arbel, Nir Peleg 
\* *Former employee; all work for this publication was done while at that organization*

The Technology Partners/Collaborators who are participating in this NCCoE project submitted their capabilities in response to a notice in the Federal Register.
Respondents with relevant capabilities or product components were invited to sign a Cooperative Research and Development Agreement (CRADA) with NIST, allowing
them to participate in a consortium to build this example solution. We are working with:

.. rst-class:: frontmatter-header
**TECHNOLOGY COLLABORATORS**


- `AMI <https://www.ami.com/>`__
- `Black Duck <https://www.blackduck.com/>`__
- `CyberArk <https://www.cyberark.com/>`__
- `Dell Technologies <https://www.dell.com/>`__
- `DigiCert <https://www.digicert.com/>`__
- `Endor Labs <https://www.endorlabs.com/>`__
- `GitLab <https://about.gitlab.com/>`__
- `Google <https://cloud.google.com/>`__
- `IBM <https://www.ibm.com/>`__
- `Microsoft <https://www.microsoft.com/>`__
- `NextLabs <https://www.nextlabs.com/>`__
- `Palo Alto Networks <https://www.paloaltonetworks.com/>`__
- `Sagittal AI <https://sagittal.ai/>`__
- `Scribe Security <https://scribesecurity.com/>`__

.. rst-class:: frontmatter-header
**DOCUMENT CONVENTIONS**

The terms “shall” and “shall not” indicate requirements to be followed strictly to conform to the publication and from which no deviation is permitted. The
terms “should” and “should not” indicate that among several possibilities, one is recommended as particularly suitable without mentioning or excluding others,
or that a certain course of action is preferred but not necessarily required, or that (in the negative form) a certain possibility or course of action is
discouraged but not prohibited. The terms “may” and “need not” indicate a course of action permissible within the limits of the publication. The terms “can” and
“cannot” indicate a possibility and capability, whether material, physical, or causal.

.. rst-class:: frontmatter-header
**CALL FOR PATENT CLAIMS**

This public review includes a call for information on essential patent claims (claims whose use would be required for compliance with the guidance or
requirements in this Information Technology Laboratory (ITL) draft publication). Such guidance and/or requirements may be directly stated in this ITL
Publication or by reference to another publication. This call also includes disclosure, where known, of the existence of pending U.S. or foreign patent
applications relating to this ITL draft publication and of any relevant unexpired U.S. or foreign patents.

ITL may require from the patent holder, or a party authorized to make assurances on its behalf, in written or electronic form, either:

a) assurance in the form of a general disclaimer to the effect that such party does not hold and does not currently intend holding any essential patent
claim(s); or

b) assurance that a license to such essential patent claim(s) will be made available to applicants desiring to utilize the license for the purpose of complying
with the guidance or requirements in this ITL draft publication either:

1. under reasonable terms and conditions that are demonstrably free of any unfair discrimination; or 

2. without compensation and under reasonable terms and conditions that are demonstrably free of any unfair discrimination. 

Such assurance shall indicate that the patent holder (or third party authorized to make assurances on its behalf) will include in any documents transferring
ownership of patents subject to the assurance, provisions sufficient to ensure that the commitments in the assurance are binding on the transferee, and that the
transferee will similarly include appropriate provisions in the event of future transfers with the goal of binding each successor-in-interest. 

The assurance shall also indicate that it is intended to be binding on successors-in-interest regardless of whether such provisions are included in the relevant
transfer documents. 

Such statements should be addressed to: nccoe-devsecops@list.nist.gov

Executive Summary
===================


In today's world, Development Operations (DevOps) represents a modern approach to software development that fosters collaboration among development, operations, and other teams that have traditionally worked in silos. This enables a software development process that delivers higher quality, reliability, agility, and efficiency. Additionally, many organizations are now integrating security into their DevOps environments, tools, and processes—a practice known as DevSecOps (Development, Security, and Operations).

In traditional software development, security was often an afterthought, tacked on at the end of the development process. DevSecOps offers a different model, one that integrates security practices from the outset and throughout the development process, adopting a "before-thought" approach rather than treating security as a separate concern in later stages or post-deployment, which is characteristic of an "after-thought" approach. There are various reasons for growing adoption of DevSecOps:

-  The growing complexity and volume of cyber threats have made software development environments prime targets for various forms of attacks and cybersecurity breaches. Bad actors are preying on overlooked security practices in software development practices, infrastructures and tools, developer endpoints, misconfigurations in cloud environments, and weak access controls that lead to vulnerabilities. DevSecOps practices are helping organizations build more resilient systems to protect against these types of threats.

-  Most software today relies on one or more components, including third-party components, yet organizations often have little or no visibility into or understanding of how these components are developed, integrated, deployed, and maintained, as well as the practices used to ensure the components’ security. DevSecOps practices automate tools to scan, identify, discover, and help eliminate vulnerabilities in third-party components early in the development lifecycle.

-  Organizations are increasingly incorporating artificial intelligence (AI) into DevSecOps to automate tasks in software development, such as code integration, testing, deployment, and monitoring. As a result, this can potentially enhance the security, efficiency, and quality of their software development processes.

While DevSecOps practices are essential for enhancing security in software development environments, implementing the `NIST Secure Software Development Framework (SSDF) <https://doi.org/10.6028/NIST.SP.800-218>`__ recommended security practices can foundationally bolster the security of the software development lifecycle. To that end, the NCCoE is undertaking a project to demonstrate and document effective DevSecOps practices that align with the SSDF. By putting the SSDF's recommendations into practice, this project will showcase examples of secure software development that strengthen DevSecOps practices at their core.

Initially, this project will focus on securing cloud-based environments that resemble typical closed-source software development settings, highlighting the dynamic enforcement of least-privileged access through a practical Zero Trust Architecture (ZTA) implementation. Moreover, the project will illustrate a holistic approach to secure software development, embedding security considerations and best practices throughout the software development lifecycle, and leveraging AI to automate builds, integrations, deliveries, and deployments, resulting in more efficient software development.

This project will provide additional insights into the potential implementations of DevSecOps that are often not available to the broader community. These insights are intended to help practitioners evaluate, compare, and identify gaps in existing software practices, ultimately enhancing cybersecurity for both software producers and consumers.

 
