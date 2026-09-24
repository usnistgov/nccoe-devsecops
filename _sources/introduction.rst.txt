Introduction 
=============


This document describes the NCCoE Secure Software Development, Security, and Operations (DevSecOps) Practices project and provides technical details on the notional reference model for DevSecOps practices, example implementations, functional demonstration scenarios, commercial technologies used, and security practices demonstrated during the project. The project’s primary objective is to demonstrate how the NIST SSDF can be applied to enhance the security of DevSecOps environments. Specifically, this project showcases example security practices and processes that align with SSDF, illustrates how their design can improve cybersecurity in software development, and documents their actual implementation using current technologies. The project’s scope encompasses the entire SDLC, from inception through final deployment and use. The project aims to demonstrate software development processes that leverage the following characteristics:

-  Shift Left: Integrates security practices earlier in the SDLC into existing processes and toolchains used by developers and managed by operations teams.

-  Automation: Automates security testing to ensure they are performed consistently and frequently throughout the development pipeline.

-  Collaboration: Various engagement practices, tools, and processes to encourage collaboration between development, security, and operations teams.

-  Pipeline with Security (Continuous Integration/Continuous Delivery (CI/CD)): Incorporates security checks into the pipeline to detect vulnerabilities early.

-  Security as Code: Manages security configurations and policies as code, allows for version control, observability, and automated deployment of security configurations.

-  Monitoring and Feedback: Software and infrastructure are continuously monitored for security vulnerabilities and checked for performance issues.

-  Vulnerability Management: Various tools and processes are in place to identify, classify, prioritize, and remediate vulnerabilities in a timely manner.

-  AI Capabilities: Various AI-enabled tools to generate code, identify and mitigate attack vectors and vulnerabilities, and perform automated security testing, code scans, and checks.

-  Zero Trust Security: Harnesses zero trust principles and approaches to secure the entire DevSecOps environment through consistent policy-driven verification, authentication, and authorization with least privilege access.

To inform and demonstrate its use case implementations, the project draws on specific guidelines, namely NIST SP 800-218 and NIST SP 800-218A. Additionally, the project has been informed by other relevant publications, including recommendations from practice guides and resources related to ZTA and AI. Given that this is a demonstrative applied research effort, it is anticipated that this project’s findings may inform future updates to NIST guidelines.

Background
----------

This document provides background information about DevSecOps, the role of AI in software development, and the role of Zero Trust in software development.

Development, Security, and Operations (DevSecOps)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DevOps is a set of processes and tools that bring together software development (Dev) and operations (Ops) teams to improve collaboration, coordination, and efficiency. This is achieved through concepts such as shared ownership, automation, and rapid feedback. DevOps activities aim to shorten development cycles, promote agile software development practices, and accelerate remediation and new feature delivery. The rise of cloud-native technologies, microservice architectures, and serverless frameworks has expanded the DevOps toolkit, and the integration of AI tools and capabilities is further evolving the DevOps landscape.

DevSecOps integrates security as a fundamental component of the DevOps model that was described earlier. By adding security to the model from the outset, essential security practices can be incorporated into the earliest stages of development, effectively “shifting left.” This approach ensures that security is a core part of DevOps practices. DevSecOps encompasses a range of practices, including security integration into software development, build and test automation, artifact packaging and distribution, and software release or deployment management. The integration of DevSecOps has the potential to: 

-  Boost Security and Reduce Risk: By embedding security into the early stages of the development lifecycle (“shift left”), DevSecOps enables early detection and remediation of vulnerabilities, reduces the risk of security breaches, and yields significant cost savings through fewer breaches and related expenses.

-  Boost Agility in Incident Response: By automating security tasks, such as vulnerability scanning, and enabling continuous monitoring and feedback, DevSecOps helps organizations quickly identify and respond to security issues. This, in turn, enables them to respond more effectively to security incidents, reducing the impact of breaches and improving overall security posture.

-  Release Software Faster and with Greater Quality: DevSecOps enables organizations to release software faster and more frequently while ensuring that security is integrated into every stage of the development process. This approach not only improves the overall quality of software by integrating security and testing, but also helps organizations demonstrate their commitment to security, ultimately enhancing customer trust and loyalty.

-  Foster Collaboration and Communication: DevSecOps promotes a cultural shift towards a more collaborative and security-aware organization, where security is everyone's responsibility. By fostering collaboration and communication between development, security, and operations teams, DevSecOps helps break down silos and improve overall efficiency.

-  Enhance Visibility, Insight, and Accountability: DevSecOps enables an environment with increased visibility, insight, and accountability into the development process, enabling organizations to track security issues and risks in real-time.

This project illustrates how the `NIST SSDF <https://doi.org/10.6028/NIST.SP.800-218>`__ practices and tasks can be implemented to enhance DevSecOps environments, helping organizations improve the security of the software they develop and operate. Additionally, the project demonstrates how to generate specific artifacts that can support and inform organizations’ evidence and declaration conformance.

This project addresses DevSecOps in the context of current and emerging secure development frameworks, practices, and tools. NIST will share lessons learned from the project with the security and software de-velopment communities to inform improvements to secure software development frameworks, prac-tices, and tools. These lessons can also inform standards development organizations’ DevSecOps-specific activities.

The Role of AI in Software Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Throughout SDLC, AI is increasingly being used to automate processes that enhance security and organizational effectiveness. AI-powered tools facilitate the automation of coding, security analysis, vulnerability detection, and remediation. The use of AI technology in software development may improve work efficiency and can lead to higher-quality software being developed in a timelier manner. However, while AI can deliver significant efficiencies and other advantages, software development teams should ensure that AI-generated content is monitored and validated by humans and that verifiable processes are in place to verify its accuracy and trustworthiness. Within DevSecOps, both human users and automated processes should oversee the adoption and use of AI. Moreover, AI-based suggestions should be subject to rigorous scrutiny by human actors to prevent uncritical acceptance. That is, there is a pressing need to implement necessary oversight to prevent the insertion of insecure and non-functional code into the software development process.

Recent advances in agentic AI expand the role of AI from providing recommendations to autonomously executing multi-step software development and DevSecOps tasks. AI agents can assist with activities such as code generation, testing, vulnerability remediation, documentation generation, and workflow orchestration across development environments. While these capabilities have the potential to accelerate the software delivery, organizations should ensure that appropriate governance, authorization controls, auditability, and human oversight are maintained for agent actions and outputs.

Identifying where AI is being used, including its use by third-party models, source code assistance, and agents, is a challenging task. To address this challenge, it is essential to provide mechanisms for tracing models, modifications, and annotations, ensuring that AI-assisted processes are subject to a level of review comparable to that of human modifications to software systems and applications. This project explores the responsible use of AI to augment existing DevSecOps tools and capabilities across the SDLC.

The Role of Zero Trust in Software Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adopting a Zero Trust security strategy significantly strengthens the resiliency of DevSecOps environ-ments. It shrinks implicit trust zones and mitigates breach risks by subjecting every access request to rigorous authentication, authorization, and device posture verification.

A combination of escalating cyber threats, remote work models, multi-cloud reliance, and strict federal compliance mandates is pushing organizations to adopt Zero Trust. Across various sectors, many organizations are already actively pursuing this strategy in the initial planning stages, and others are well into implementation.

To strengthen DevSecOps security, this project explores Zero Trust principles and demonstrates how to apply them across the development lifecycle through measures such as:

-  Enforcing strict, policy-based access and security controls.
-  Implementing continuous monitoring, verification, and vulnerability scanning.
-  Ensuring artifact integrity and verifying code commits and signatures.
-  Employing proactive security measures at every stage.

Audience
--------

The audience for this publication is technology leaders and practitioners responsible for developing, delivering, and operating secure software systems. This group includes software developers, software systems designers, software development managers, software security specialists, software acquisition specialists and managers, and systems managers and owners. Furthermore, this publication will be of interest to those responsible for enhancing collaboration between software development, operations, and security teams to maintain agility and innovation while strengthening security. Readers are assumed to understand basic DevSecOps concepts.

Scope
-----

This project focuses on demonstrating and documenting the application of the NIST Secure Software Development Framework (SSDF) to enhance the security of DevSecOps processes in cloud-based environments. The capabilities being demonstrated are applicable to information technology (IT) development for medium- to large-sized enterprises across multiple sectors. The initial focus will be on constructing environments that mimic representative closed-source software development environments, that is, environments that resemble those implemented by organizations that have a vested interest in protecting their intellectual property from outside tampering/observation. The development of open-source software may be addressed in a later phase of this project. Furthermore, Zero Trust principles and approaches described in NIST Special Publication 800-207 are integrated to elevate the security posture of DevSecOps. 

This project will not focus on a particular type of software, but on the process of developing software in general. Certain domains pertaining to the following NCCoE projects, such as `Operational Technology
(OT) <https://www.nccoe.nist.gov/manufacturing#nccoe-operational-technology-security-series>`__, `Internet of Things (IoT) <https://www.nccoe.nist.gov/iot>`__,
and `Applied Cryptography <https://www.nccoe.nist.gov/applied-cryptography>`__, are out of scope for this project. While the project will investigate the use of
AI tools in the DevSecOps lifecycle, it will not specifically address machine learning operations (MLOps) or AI bill of materials (AI BOM). Along the same lines, addressing privacy-related concerns is not within the scope of this project, but organizations should address them in their implementations.

Challenges
----------

As software development becomes increasingly complex and fast-paced, it's crucial to strike a balance between leveraging innovation and ensuring cybersecurity. This project aims to address the following key challenges in secure software development:

1. Identification and Mitigation of Vulnerabilities: Modern software development is dynamic and complex because it involves a wide range of tools, automations, ecosystems, and services from a wide variety of sources. As a result, identifying and mitigating all potential security vulnerabilities is challenging.

2. Use of Third-Party and Open-Source Components: The widespread use of third-party and open-source components in modern software development can introduce security risks if not properly managed and maintained.

3. Exposing APIs: The expanding use of APIs for external integration poses substantial security challenges, including the risk of unauthorized access and data breaches.

4. Producing Evidence for Software Composition and Provenance: Manual and ad hoc evidence generation can result in inconsistencies, scalability issues, and heightened security risks, such as vulnerability exploitation, supply chain attacks, and component tampering, stemming from a lack of transparency, transient build dependencies, and potentially manipulated provenance records.

5. Code Signing: Binary or code signing poses significant security challenges, including private key management, certificate management, and the risk of signed malicious code.

6. Emergence of AI tools: AI tools are being increasingly employed throughout the software development process. While there are potential applications in code generation, code evaluation, security monitoring, and other areas, the risks associated with employing these technologies insecurely are not yet fully understood.

This project will address these challenges by demonstrating and documenting example security practices and their implementations, to help organizations effectively address them.


How to Use This Guide
---------------------
 
The primary objective of this project is to demonstrate how the NIST SSDF can be applied to enhance DevSecOps security using currently available technologies. To achieve this, the project executes four primary tasks, which this document details in sequence. First, it describes a collaboratively developed Notional Reference Model for DevSecOps (Section 2) to establish the groundwork for how the project interprets DevSecOps processes and flow in its demonstrations. Second, it maps SSDF practices at a high level to the model’s phases to provide insight into when each practice is performed (Section 3). Third, it outlines detailed architectures for each example implementation constructed as part of the project (Section 4). Finally, it presents specific scenarios—called Functional Demonstrations—used to execute activities during each SDLC phase, highlighting how selected capabilities were exercised (Section 5). Derived directly from the reference model, these functional demonstrations outline detailed Demonstration Steps, Components, Expected Outcomes, and—most importantly—the related SSDF practices and tasks. This document is organized as follows: 

-  :ref:`Executive Summary: <executive_summary>` Provides a high-level overview of this guide.
-  :doc:`Section 1 – Introduction: <introduction>` Provides an overview of the NCCoE’s “Secure Software Development, Security, and Operations (DevSecOps) Practices” project. It includes the project background, the intended audience, the project scope, and the identification of challenges faced in secure software development.
-  :doc:`Section 2 - Notional Reference Model for DevSecOps for demonstration of NIST SSDF: <notational-reference-model>` Provides a notional reference model developed by the project team and its collaborators. 
-  :doc:`Section 3 – Mapping SSDF to the Notional Reference Model: <mapping-ssdf>` Provides the relationship between the SSDF and NCCoE’s Notional Reference Model for DevSecOps 
-  :doc:`Section 4 – Example Implementations: <example-implementations>` Provides a technical overview of each example implementation implemented at the NCCoE.
-  :doc:`Section 5 – Functional Demonstrations: <functional-demonstrations>` Provides the use-case scenarios and results demonstrated by the NCCoE.
-  :doc:`Section 6 – Next Steps: <next-steps>` Provides a summary of the project's next steps.
-  :doc:`Appendix A – <appendix-a>` Provides a list of acronyms.
-  :doc:`Appendix B – <appendix-b>` Provides description of the components used in the notional reference model.
-  :doc:`Appendix C – <appendix-c>` Provides a detailed analysis of the SSDF.
-  :doc:`Appendix D – <appendix-d>` Provides collaborators and their contributions.
-  :doc:`Appendix E – <appendix-e>` Provides changes made to this document through the revisions.

