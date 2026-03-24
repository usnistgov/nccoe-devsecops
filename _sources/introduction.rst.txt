Introduction 
=============


This document provides an overview of the NCCoE Secure Software Development, Security, and Operations (DevSecOps) Practices project. The project's primary objective is to demonstrate the application of the NIST SSDF to enhance the security of DevSecOps environments. Specifically, this project showcases example security practices and processes that align with SSDF, illustrates how their design can improve cybersecurity in software development, and documents their actual implementation using current technologies. The project's scope encompasses the entire software development lifecycle, from inception to final deployment. The project aims to demonstrate software development processes that leverage the following characteristics:

-  Shift Left: Integrates security practices earlier in the software development lifecycle into existing processes and toolchains used by developers and managed by operations teams.

-  Automation: Automates security testing to ensure they are performed consistently and frequently throughout the development pipeline.

-  Collaboration: Various engagement practices, tools, and processes to encourage collaboration between development, security and operations teams.

-  Pipeline with Security (Continuous Integration / Continuous Delivery (CI/CD): Incorporates security checks into pipeline to identify vulnerabilities early.

-  Security as Code: Manages security configurations and policies as code, allows for version control, and automated deployment of security configurations.

-  Monitoring and Feedback: Software and infrastructure are continuously monitored for security vulnerabilities and checked for performance issues.

-  Vulnerability Management: Various tools and processes in place to identify, classify, prioritize, and remediate vulnerabilities in a timely manner.

-  AI Capabilities: Various AI-enabled tools to identify and mitigate attack vectors and vulnerabilities, and perform automated security testing, code scans, and checks.

-  Zero Trust Security: Harnesses zero trust principles and approaches to secure the entire DevSecOps environment through consistent policy driven verification, authentication, and authorization with least privilege access.

To inform and demonstrate its use case implementations, the project draws on specific guidelines, namely NIST SP 800-218 and NIST SP 800-218A. Additionally, the project has been informed by other relevant publications, including recommendations from practice guides and resources related to ZTA and AI. Given that this is a demonstrative applied research effort, it is anticipated that this project’s findings may inform future updates to NIST guidelines.

Background
----------

This section provides background information about DevSecOps, the role of AI in software development, and the role of Zero Trust in software development.

Development, Security, and Operations (DevSecOps)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Development Operations (DevOps) is an organizational model that brings together software development and operations teams to improve collaboration, coordination, and efficiency. This is achieved through concepts such as shared ownership, automation, and rapid feedback. DevOps activities aim to shorten development cycles, promote agile software development practices, and increase the pace of remediations and new features. The rise of cloud-native technologies, microservice architectures, and serverless frameworks has expanded the DevOps toolkit, and the integration of AI tools and capabilities is further evolving the DevOps landscape.

DevSecOps integrates security as a fundamental component of the DevOps model that was described earlier. By adding security to the model from the outset, essential security practices can be incorporated into the earliest stages of development, effectively “shifting left.” This approach ensures that security is a core part of DevOps practices. DevSecOps encompasses a range of practices, including security integration into software development, build and test automation, artifact packaging and distribution, and software release or deployment management. The integration of DevSecOps has the potential to: 

-  Boost Security and Reduce Risk: By embedding security into the early stages of development lifecycle (“shift left”), DevSecOps facilitates the early detection and remediation of vulnerabilities, reduces the risk of security breaches, and yields significant cost savings resulting from fewer security breaches and related expenses.

-  Boost Agility in Incident Response: By automating security tasks, such as vulnerability scanning, and enabling continuous monitoring and feedback, DevSecOps helps organizations quickly identify and respond to security issues. This, in turn, enables them to respond more effectively to security incidents, reducing the impact of breaches and improving overall security posture.

-  Release Software Faster and with Greater Quality: DevSecOps enables organizations to release software faster and more frequently while ensuring that security is integrated into every stage of the development process. This approach not only improves the overall quality of software by integrating security and testing, but also helps organizations demonstrate their commitment to security, ultimately enhancing customer trust and loyalty.

-  Foster Collaboration and Communication: DevSecOps promotes a cultural shift towards a more collaborative and security-aware organization, where security is everyone's responsibility. By fostering collaboration and communication between development, security, and operations teams, DevSecOps helps break down silos and improve overall efficiency.

-  Enhance Visibility, Insight and Accountability: DevSecOps enables an environment with increased visibility, insight and accountability into the development process, enabling organizations to track security issues and risks in real-time.

This project illustrates how the `NIST SSDF <https://doi.org/10.6028/NIST.SP.800-218>`__ practices and tasks can be implemented to enhance DevSecOps environments to aid organizations in improving the security of the software they develop and operate. Additionally, the project demonstrates how to generate specific artifacts that can support and inform organizations’ evidence and declaration conformance.

This project addresses DevSecOps in the context of current and emerging secure development frameworks, practices, and tools. NIST will share lessons learned during the project with security and software development communities with the intent of informing improvements to secure software development frameworks, practices, and tools. These lessons can also inform standards development organizations’ DevSecOps-specific activities.

The Role of AI in Software Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Throughout the software development lifecycle, AI is increasingly being used to automate processes that enhance security and organizational effectiveness. AI-powered tools facilitate the automation of coding, security analysis, and vulnerability detection and remediation. The use of AI technology in software development improves work efficiency and can lead to higher-quality software being developed in a timelier manner. However, while AI can deliver significant efficiencies and other advantages, software development teams should ensure that AI-generated content is monitored and validated by humans, and verifiable processes are in place to ensure its accuracy and trustworthiness. Within DevSecOps, both human users and automated processes should oversee the adoption and use of AI. Moreover, AI-based suggestions should be subject to rigorous scrutiny by human actors to prevent uncritical acceptance. There is a pressing need to implement necessary oversight to prevent the insertion of insecure and non-functional code into the software development process.

Identifying where AI is being used, including its use by third-party models, in source code, and in agents, is a challenging task. To address this challenge, it is essential to provide mechanisms for tracing models, modifications, and annotations, ensuring that AI-assisted processes are subject to a level of review comparable to that of human modifications to software systems and applications. This project explores the responsible use of AI to augment existing DevSecOps tools and capabilities across the software development lifecycle.

The Role of Zero Trust in Software Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Zero Trust security strategy, if adopted, can significantly strengthen the resiliency of DevSecOps environments by shrinking implicit trust zones and mitigating breach risks through subjecting every access request to rigorous authentication, and authorization, and device security posture. Escalating cybersecurity threats, a rise in remote and hybrid working options, increased reliance on cloud services and multi-cloud environments, and data protection requirements and measures, along with federal mandates for cybersecurity, push organizations to adopt zero trust as their resilient cybersecurity strategy for today’s hybrid environments. Many organizations are actively pursuing Zero Trust, some in the initial planning stages and others well into implementation across various sectors.

To strengthen the security of the DevSecOps process, this project will explore the use of Zero Trust principles and approaches and demonstrate the utilization of access control, security checks and controls, continuous monitoring and scanning for vulnerabilities, ensuring the integrity of artifacts, verifying code commits and signatures, and employing other proactive security measures throughout the development lifecycle.

Audience
--------

The audience for this publication is technology leaders and practitioners responsible for developing, delivering, and operating secure software systems. This group includes software developers, software systems designers, software development managers, software security specialists, software acquisition specialists and managers, and systems managers and owners. Furthermore, this document will be of interest to those responsible for enhancing collaboration between software development, operations, and security teams to maintain agility and innovation while strengthening security. Readers are assumed to understand basic DevOps and secure software development concepts.

Scope
-----

There are many methodologies used to produce software. This project focuses on demonstrating and documenting the application of the NIST Secure Software Development Framework (SSDF) to enhance the security of DevSecOps processes in cloud-based environments. The capabilities being demonstrated are applicable to information technology (IT) development in medium to large enterprises in multiple sectors. The initial focus will be constructing environments that mimic representative closed-source software development environments, that is, environments that resemble those implemented by organizations that have a vested interest in protecting their intellectual property from outside tampering/observation. The development of open-source software may be addressed in a later phase of this project. Furthermore, Zero Trust principles and approaches will be also integrated to elevate the security posture of the DevSecOps lifecycle. 

This project will not focus on the development of any particular technology type (i.e., the output of the software development process). Certain domains
pertaining to the following NCCoE projects such as `Operational Technology
(OT) <https://www.nccoe.nist.gov/manufacturing#nccoe-operational-technology-security-series>`__, `Internet of Things (IoT) <https://www.nccoe.nist.gov/iot>`__,
and `Applied Cryptography <https://www.nccoe.nist.gov/applied-cryptography>`__ are out of scope for this project. While the project will investigate the use of
AI tools in the DevSecOps lifecycle, it will not specifically address machine learning operations (MLOps) or AI bill of material (AI BOM). Along the same lines, addressing privacy-related concerns is not within the scope of this project, but organizations should address them in their implementations.

Challenges
----------

As software development becomes increasingly complex and fast-paced, it's crucial to strike a balance between leveraging innovation and ensuring cybersecurity. This project aims to address the following key challenges in secure software development:

1. Identification and Mitigation of Vulnerabilities: Modern software development is complex because it involves a wide range of tools, automations, ecosystems, and services. As a result, identifying and mitigating all potential security vulnerabilities is challenging.

2. Use of Third-Party and Open-Source Components: The widespread use of third-party and open-source components in modern software development can introduce security risks if not properly managed and maintained.

3. Exposing APIs: The expanding use of APIs for external integration poses substantial security challenges, including the risk of unauthorized access and data breaches.

4. Producing Evidence for Software Composition and Provenance: Manual and ad hoc evidence generation can result in inconsistencies, scalability issues, and heightened security risks, such as vulnerability exploitation, supply chain attacks, and component tampering, stemming from a lack of transparency and potentially manipulated provenance records.

5. Code Signing: Binary or code signing poses significant security challenges, including private key management, certificate management, and the risk of signed malicious code.

6. Emergence of AI tools: AI tools are being increasingly employed throughout the software development process. While there are potential applications in code generation, code evaluation, security monitoring, and other aspects, the risks associated with employing these technologies insecurely are not yet fully understood.

This project will address these challenges by demonstrating and documenting example security practices and their implementations, to help organizations effectively address them.
