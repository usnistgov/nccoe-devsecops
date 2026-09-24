Appendix C SSDF Analysis :bdg-primary:`New`
===============================================

This appendix analyzes the SSDF in the context of this project. For each task, we identify key objectives that align with SSDF recommendations and outline actionable approaches to achieve them—insights that directly informed our demonstration architecture. This analysis is purely illustrative for this project and is not intended as a normative interpretation or formal extension of the framework.

C.1. Prepare the Organization (PO)
----------------------------------

C.1.1. PRACTICE (PO.1) - Define Security Requirements for Software Development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that security requirements for software development are known at all times so they can be taken into account throughout the SDLC, and to minimize
duplication of effort by collecting requirements information once and sharing it. This includes requirements from internal sources (e.g., the organization’s
policies, business objectives, and risk management strategy) and external sources (e.g., applicable laws and regulations).

**Task PO.1.1**

Identify and document all security requirements for the organization’s software development infrastructures and processes, and maintain the requirements over
time.

**Key Objectives:**

This task has two key objectives:

1. **The identification and documentation of security policies, requirements, and processes for software development infrastructure and processes, and
   maintaining them over time.**

..

   **Analysis:**

   To achieve this objective, organizations may consider establishing and maintaining security policies and requirements for their Software Development Life
   Cycle (SDLC). This process typically begins with a comprehensive discovery and identification phase to establish a baseline of the current environment and
   risk profile. This is followed by a process to define policies for securing software development infrastructure, components (including open-source and
   third-party software), and processes, as well as to regularly review and update security requirements in response to new mandates or major security
   incidents. To effectively implement these policies, organizations may conduct risk assessments to inform the development of clear, concise, and comprehensive
   security policies that address identified risks and threats. This involves establishing a security governance framework that defines roles, responsibilities,
   and accountability for security decision-making and oversight, including implementing security controls by integrating security into every stage of the
   software development cycle and its corresponding infrastructure, from design to deployment.

   Furthermore, to maintain the security requirements for software development infrastructure and processes over time, organizations can identify and integrate
   a solution that leverages appropriate tools and technologies, along with the necessary processes for regularly reviewing and updating security requirements,
   particularly in response to new requirements, major security incidents, or on an annual basis.

2. **The establishment of effective communication and awareness strategies.**

..

   **Analysis:**

   To achieve this objective, organizations can use effective communication and awareness strategies to ensure that relevant stakeholders are informed about
   changes to requirements, an important aspect of change management and communication.

   Note: The specific approaches to establishing effective communication and awareness strategies for all personnel are beyond the scope of this project's
   demonstration, given the variability in organizational structures and established processes.

**Task PO.1.2**

Identify and document all security requirements for organization-developed software to meet and maintain the requirements over time.

**Key Objectives:**

This task has two key objectives:

1. **The identification and documentation of security requirements for organization-developed software.**

..

   **Analysis:**

   To implement this objective, organizations can establish policies that specify risk-based software architecture and design requirements. This includes making
   code modular to facilitate code reuse and updates, isolating security components from other components during execution, and avoiding undocumented commands
   and settings. Organizations can also define security requirements for their software and verify compliance at key points in the Software Development Life
   Cycle (SDLC), such as through gates that check for classes of software flaws or responses to vulnerabilities discovered in released software. Furthermore,
   analyzing the risk of applicable technology stacks, including languages, environments, and deployment models, can help organizations identify and mitigate
   potential risks and recommend or require the use of stacks that will reduce risk compared to others.

2. **The maintenance of the security requirements for organization-developed software.**

..

   **Analysis:**

   To implement this objective, organizations can conduct regular reviews and updates of security requirements, as well as a clear process for handling
   exceptions.

**Task PO.1.3**

Communicate requirements to all third parties who will provide commercial software components to the organization for reuse by the organization’s own software.

**Key Objectives:**

This task has three key objectives:

1. **The identification and documentation of security requirements and criteria for third parties.**

..

   **Analysis:**

   To implement this objective, organizations can establish a clear foundation by defining security requirements and criteria. This involves defining a core set
   of security requirements that software components (e.g., libraries, frameworks, open-source software, and commercial off-the-shelf (COTS) software) acquired
   from external sources must adhere to, thereby ensuring a baseline level of security assurance. These requirements can be incorporated into contractual
   agreements, such as software contracts and acquisition documents, to hold third-party vendors accountable for delivering secure software. Furthermore,
   organizations can establish security-related evaluation criteria for software selection, including factors such as the vendor's vulnerability disclosure and
   response processes, secure coding practices, and compliance with industry-recognized security standards. By establishing these requirements and criteria,
   organizations can ensure they acquire software that meets their security needs.

2. **The confirmation of third-party compliance and accountability.**

..

   **Analysis:**

   To implement this objective, organizations can require third-party vendors to demonstrate compliance. This can be achieved by requiring third-party vendors
   to attest that their software meets a set of core security requirements established by the organization. Additionally, organizations can require vendors to
   provide provenance data and integrity verification mechanisms for all software components. This provides transparency into the software's development and maintenance, allowing organizations to make informed decisions about the software they
   acquire.

3. **The management of these risks and exceptions.**

..

   **Analysis:**

   To implement this objective, organizations can establish and follow processes to address exceptions and manage risk. This includes conducting periodic
   reviews of all approved exceptions to ensure that the risks associated with non-compliant software components are regularly assessed and mitigated. By having
   a structured risk management process in place, organizations can effectively manage these risks and maintain their overall security posture.

C.1.2. PRACTICE (PO.2) - Implement Roles and Responsibilities:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that everyone inside and outside of the organization involved in the SDLC is prepared to perform their SDLC-related roles and responsibilities throughout
the SDLC.

**Task PO.2.1**

Create new roles and alter responsibilities for existing roles as needed to encompass all parts of the SDLC. Periodically review and maintain the defined roles
and responsibilities, updating them as needed.

**Key Objectives:**

This task has two key objectives:

1. **The identification and documentation of roles and responsibilities for the members of the relevant teams involved in the SDLC.**

..

   **Analysis:**

   To implement this objective, organizations can define roles and responsibilities for the relevant teams involved in the SDLC. This includes integrating
   security roles into these teams and assigning specific responsibilities to stakeholders such as cybersecurity staff, security champions, project managers,
   senior management, software developers, testers, assurance leads, product owners, operations teams, site reliability engineers, and platform engineers.

2. **The maintenance of the roles and responsibilities for the members of the relevant teams involved in the SDLC.**

..

   **Analysis:**

   To achieve this objective, organizations can establish a process to periodically review and manage these roles as necessary to ensure they remain relevant
   and effective.

**Task PO.2.2**

Provide role-based training for all personnel with responsibilities that contribute to secure development. Periodically review personnel proficiency and
role-based training, and update the training as needed.

**Key Objectives:**

This task has two key objectives:

1. **The identification, documentation, and creation of role-based training for all personnel involved in secure software development.**

..

   **Analysis:**

   To achieve this objective, organizations can identify and document the desired training outcomes for each role and define the type of training or curriculum
   required to achieve them. They can then create tailored training plans for each role and acquire or develop the necessary training content, customizing it as
   needed to meet the organization's specific needs.

2. **The maintenance of the relevance and effectiveness of role-based training over time.**

..

   **Analysis:**

   Organizations can measure the outcome performance of the training to identify areas for improvement, informing future adjustments to the training program to
   ensure it remains effective and relevant.

   Note: The specific approaches for identifying, documenting, and creating role-based training for all personnel are beyond the scope of this project's
   demonstration, given the variability in organizational structures and established processes.

**Task PO.2.3**

Obtain upper management or authorizing official commitment to secure development and convey that commitment to all with development-related roles and
responsibilities.

**Key Objectives:**

This task has one key objective:

1. **The identification and appointment of a single leader or leadership team as a liaison to oversee the secure software development process.**

..

   **Analysis:**

   To achieve this objective, organizations can appoint a single leader or a leadership team to oversee the secure software development process, delegating
   responsibilities as needed, and being accountable for software releases. They can raise awareness among authorizing officials about the risks associated with
   insecure software development and the benefits of integrating security throughout the development life cycle. Furthermore, they can support upper management
   in communicating the importance of secure development to personnel in development-related roles and in educating them about upper management's commitment to
   secure development.

   Note: The specific approaches to identify and appoint a single leader or leadership team to facilitate communication and cooperation between upper management
   and development teams are beyond the scope of this project's demonstration, given the variability in organizational structures and established processes.

C.1.3. PRACTICE (PO.3) - Implement Supporting Toolchains:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use automation to reduce human effort and improve the accuracy, reproducibility, usability, and comprehensiveness of security practices throughout the SDLC, as
well as provide a way to document and demonstrate the use of these practices. Toolchains and tools may be used at different levels of the organization (e.g.,
organization-wide or project-specific) and may address a particular part of the SDLC, such as a build pipeline.

**Task PO.3.1**

Specify which tools or tool types must or should be included in each toolchain to mitigate identified risks, as well as how the toolchain components are to be
integrated with each other.

**Key Objectives:**

This task has three key objectives:

1. **The definition and identification of toolchain categories and their required tools, including security tools for integration into the developer
   toolchain.**

..

   **Analysis:**

   To achieve this objective, organizations can implement a structured approach to toolchain management by defining toolchain categories, identifying the
   required tools for each category, and integrating security tools through standardized interfaces and data formats.

2. **The maintenance of immutable records and logs for auditability.**

..

   **Analysis:**

   To achieve this objective, organizations can assess tool signing capabilities to ensure tamper-evident records and logs, thereby supporting auditability and
   compliance.

3. **The implementation of a solution for toolchain management and orchestration.**

..

   **Analysis:**

   To achieve this objective, organizations can implement an automation solution to enable streamlined toolchain management and orchestration, enhancing process
   efficiency and reducing errors.

**Task PO.3.2**

Follow recommended security practices when deploying, operating, and maintaining tools and toolchains.

**Key Objectives:**

This task has three key objectives:

1. **The deployment of security tools and toolchains, and the integration with existing tools and software development processes.**

..

   **Analysis:**

   To achieve this objective, organizations can leverage the defined toolchain categories and tools to evaluate, select, and acquire the necessary technologies
   that enable them. Furthermore, organizations can integrate these technologies with other tools, existing processes, and workflows. During implementation,
   organizations can leverage code-based configurations, such as Toolchains as Code (TaC) or Pipelines as Code (PaC), to enable version control and promote
   reusability and consistency.

2. **The implementation of technologies and deterministic processes to enable reproducible builds.**

..

   **Analysis:**

   To achieve this objective, organizations can implement software development practices that ensure consistent, reproducible builds, producing identical binary
   or executable output across environments and machines when using the same code.

3. **The maintenance of the tools and toolchains.**

..

   **Analysis:**

   To achieve this objective, organizations can leverage their toolchain management and orchestration solution to manage toolchains. Additionally, organizations
   can continuously monitor tools and their logs for operational and security issues, and regularly verify each tool's integrity and provenance to identify
   potential problems. Furthermore, organizations can also establish processes to update, upgrade, or replace tools for security reasons as necessary.

**Task PO.3.3**

Configure tools to generate artifacts of their support of secure software development practices as defined by the organization.

**Key Objectives:**

This task has two key objectives:

1. **The implementation of audit trails and scheduled audits for existing tooling, and the establishment of necessary processes to support continuous
   improvement.**

..

   **Analysis:**

   To achieve this objective, organizations can establish a robust monitoring and auditing framework by implementing audit trails for existing tooling, enabling
   them to track and monitor secure software development actions. Additionally, organizations can implement necessary processes and procedures to facilitate
   regularly scheduled audits, which will not only ensure compliance but also drive continuous improvement by identifying areas for enhancement and optimizing
   their SDLC.

2. **The establishment and enforcement of security and retention policies for artifacts, and the assignment of responsibility for creating required artifacts
   that tools cannot generate.**

..

   **Analysis:**

   To achieve this objective, organizations can develop and enforce comprehensive security and retention policies for artifact data to ensure its integrity,
   confidentiality, and availability. This includes defining procedures for data classification, storage, and disposal to prevent unauthorized access or data
   loss. Furthermore, organizations can assign roles and responsibilities for generating artifacts that cannot be automatically produced by existing tools,
   ensuring that the necessary personnel are accountable for creating and maintaining these critical artifacts.

C.1.4. PRACTICE (PO.4) - Define and Use Criteria for Software Security Checks:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help ensure that the software resulting from the SDLC meets the organization’s expectations by defining and applying criteria to assess the software’s security
during development.

**Task PO.4.1**

Define criteria for software security checks and track them throughout the SDLC.

**Key Objectives:**

This task has two key objectives:

1. **The definition of criteria for software security checks.**

..

   **Analysis:**

   To achieve this objective, organizations can establish clear criteria to measure the effectiveness of their security risk management. This can be done by
   defining relevant metrics, such as Key Performance Indicators (KPIs), Key Risk Indicators (KRIs), and vulnerability severity scores, to assess and manage
   security and risk posture throughout the Software Development Life Cycle (SDLC). Additionally, organizations can enhance their existing security checks by
   incorporating a clear and concise description of the requirements that must be met for the work to be considered complete. These requirements may include
   code quality checks, testing, code reviews, documentation, verification, and other relevant criteria.

2. **The tracking of progress toward meeting these criteria throughout the SDLC.**

..

   **Analysis:**

   To achieve this objective, organizations can review the artifacts generated through the software development workflow system to determine whether they meet
   the established criteria. Additionally, organizations can record security check approvals, rejections, and exception requests within the workflow and
   tracking system, and establish a process to analyze the collected data to improve security throughout the SDLC.

**Task PO.4.2**

Implement processes and mechanisms to gather and safeguard the necessary information to support the criteria.

**Key Objectives:**

This task has two key objectives:

1. **The implementation of processes and mechanisms to automatically gather pertinent information.**

..

   **Analysis:**

   To achieve this objective, organizations can leverage their toolchain to automatically gather pertinent information to inform security decision-making and
   deploy additional tools as needed to generate and collect data that support the established criteria. Furthermore, organizations can automate decision-making
   processes driven by criteria and regularly review them to ensure their effectiveness.

2. **The safeguarding of all pertinent information.**

..

   **Analysis:**

   To achieve this objective, organizations can restrict access to authorized personnel only, with security controls in place to prevent unauthorized alteration
   or deletion.

C.1.5. PRACTICE (PO.5) - Implement and Maintain Secure Environments for Software Development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that all components of software development environments are strongly protected from internal and external threats to prevent compromises of the
environment or the software being developed or maintained within it. Examples of software development environments include development, build, test, and
distribution.

**Task PO.5.1**

Separate and protect each environment involved in software development.

**Key Objectives:**

This task has four key objectives:

1. **The isolation of environments from each other and from production environments, and the minimization of the use of production-environment software and
   services in non-production environments.**

..

   **Analysis:**

   To achieve this objective, organizations can implement network segmentation and access controls to isolate environments from each other and from production
   environments, as well as to separate components within non-production environments, thereby reducing attack surfaces, limiting lateral movement, and
   preventing privilege escalation. Additionally, organizations can minimize the use of production-environment software and services from non-production
   environments, further reducing the risk of unauthorized access or data breaches and maintaining a robust security posture across all environments.

2. **The implementation of strong authentication and authorization mechanisms to control access to environments and minimize human access to sensitive
   systems.**

..

   **Analysis:**

   To achieve this objective, organizations can implement a robust access control strategy that incorporates multi-factor, risk-based authentication and
   conditional access. This involves enforcing strict authentication protocols, limiting connections to and from each environment, and restricting internet
   access to only necessary resources. Additionally, organizations can minimize human access to critical toolchain systems, such as build services, and maintain
   continuous monitoring and auditing of all access attempts and privileged access usage to ensure the security and integrity of the development environments.

3. **The monitoring and logging of activities within the environment, including trust relationships, operations, and security controls.**

..

   **Analysis:**

   To achieve this objective, organizations can implement a comprehensive monitoring and logging strategy. This involves regular logging, monitoring, and
   auditing trust relationships and access between environments and components, as well as continuously logging and monitoring operations and alerts across all
   development environment components to detect and respond to cyber incidents. Additionally, organizations can configure security controls and other tools to
   generate activity logs and artifacts, enabling thorough incident response and recovery.

4. **The adoption of a zero-trust security approach to mitigate vulnerabilities in software across all environments and software development infrastructure.**

..

   **Analysis:**

   To achieve this objective, organizations can implement a proactive vulnerability management strategy and a zero trust architecture. This involves
   continuously monitoring software deployed across all environments for new vulnerabilities and responding to them in a risk-based manner. Additionally,
   organizations can configure and implement measures to secure the environment's hosting infrastructure, following a zero-trust architecture that assumes no
   inherent trust and verifies all access and interactions.

**Task PO.5.2**

Secure and harden development endpoints (e.g., for software designers, developers, testers, builders) to perform development-related tasks using a risk-based
approach.

**Key Objectives:**

This task has three key objectives:

1. **The configuration and hardening of development endpoints to prevent unauthorized access to ensure a secure environment.**

..

   **Analysis:**

   To achieve this objective, organizations should review existing hardening guides and determine the rules that best align with organizational needs. Hardening
   guides are produced by various entities, including hardware and software vendors and government agencies. Popular hardening guides are the Security Technical
   Implementation Guides (STIGs) published by the Defense Information Systems Agency (DISA).

   Once specific hardening rules have been selected, the organization should secure each endpoint by implementing the rules and verifying compliance. Producing
   proof of such compliance is recommended, as it can support future needs when an organization needs to show that its endpoints are, in fact, hardened. A
   spreadsheet with each rule and the actual setting on the endpoint is one way to accomplish this.

2. **The confirmation that users and services have the necessary authentication and authorization to control access to development endpoints and resources.**

..

   **Analysis:**

   To achieve this objective, organizations should verify individual access to the development endpoints and leverage multi-factor authentication to confirm
   identity. By following authentication best practices and the principle of least privilege, development endpoints can be protected from many adversarial
   activities.

3. **The monitoring and logging of activities related to development endpoints, to detect and respond to potential security incidents.**

..

   **Analysis:**

   To achieve this objective, organizations should record events throughout the development lifecycle and continuously review them to identify areas for
   improvement. Events to monitor include system failures, access requests, system interactions, system use, and known exploit attempts. Speedy response to each
   event, along with improvements to prevent future unwanted events, will help improve overall security within the environment during the entire lifecycle.

C.2. Protect Software (PS)
--------------------------

C.2.1. PRACTICE (PS.1) - Protect All Forms of Code from Unauthorized Access and Tampering:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help prevent unauthorized changes to code, whether inadvertent or intentional, that could circumvent or negate the software's intended security characteristics.
For code that is not intended to be publicly accessible, this helps prevent the theft of the software and may make it more difficult or time-consuming for
attackers to find vulnerabilities in the software.

**Task PS.1.1**

Store all forms of code – including source code, executable code, and configuration as code – based on the principle of least privilege so that only authorized
personnel, tools, and services have access.

**Key Objectives:**

This task has two key objectives:

1. **The avoidance of unexpected (and potentially malicious) changes to the software.**

..

   **Analysis:**

   The first objective of this task is to maintain control over the software and track changes made to it in support of future comparison and recovery. An
   important part of software development is limiting who is allowed to edit the source code so that individuals who are not sufficiently trained or those
   seeking to inflict harm by altering functionality cannot modify the code. Additionally, when a problem is discovered, it is important to be able to examine
   who made the change and when it occurred, and roll back to known good versions if necessary. All this functionality is achieved using a version control
   system.

   Using a version control system to limit who can make changes to the code, while also associating each change with the individual who made it, enables the
   development team to take corrective actions when an issue is discovered during a review (see Task PW.7.2) or testing (see Task PW.8.2) activity. Issues
   discovered in certain functionality or in specific areas of the code can be examined by reviewing the historical changes to the relevant code. Developer
   training can be tailored to individual needs based on who is making mistakes and the types of mistakes being made. Consistently problematic areas of source
   code can be easily identified and submitted for additional review and testing.

   A version control system also provides the protections needed to limit who is allowed to change the source code. Developers are registered with the system,
   and only those approved are granted authorization to submit changes. This least-privilege principle protects the software from arbitrary changes by
   individuals not associated with the development, who might alter the code in an unexpected or malicious way.

   To successfully achieve this objective, the development team should complete the installation and use of a version control system.

2. **The prevention of theft of the code.**

..

   **Analysis:**

   A second objective of this task is to prevent unauthorized individuals from acquiring the source code and using it to create competing software or to
   identify weaknesses that could be used to attack the software. A proper version control system can again be used to accomplish this objective, as it provides
   authorization mechanisms to control access. To be successful, the version control system must be configured appropriately with authentication best practices
   in place. Mechanisms such as multifactor authentication and encrypted communication protocols are critical to the success of the authorization system.

C.2.2. PRACTICE (PS.2) - Provide a Mechanism for Verifying Software Release Integrity:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help software acquirers ensure that the software they acquire is legitimate and has not been tampered with.

**Task PS.2.1**

Make software integrity verification information available to software acquirers.

**Key Objectives:**

This task has one key objective:

1. **The avoidance of a tainted (and potentially malicious) version of the software being mistaken as legitimate.**

..

   **Analysis:**

   The objective of this task is to ensure that the end user can verify that the software being delivered has not been altered during the supply chain process.
   To accomplish this, the development team should provide an integrity-checking mechanism, such as a digital signature, a cryptographic checksum, or a hash of
   the files being delivered. The end user can then check the delivered software using this integrity check and identify tainted files that don’t match what the
   development team produced.

   Care must be taken in how the integrity check information is delivered to the end user. Public-key encryption that is part of effective digital signature
   implementations is recommended. Additionally, organizations might want to consider including information about how, where, and under what controls software
   was produced.

C.2.3. PRACTICE (PS.3) - Archive and Protect Each Software Release:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preserve software releases in order to help identify, analyze, and eliminate vulnerabilities discovered in the software after release.

**Task PS.3.1**

Securely archive the necessary files and supporting data (e.g., integrity verification information, provenance data) to be retained for each software release.

**Key Objectives:**

This task has one key objective:

1. **Preservation of software artifacts in support of future analysis and maintenance activities.**

..

   **Analysis:**

   The objective of this task is to securely store all artifacts used to create a release. This includes source code, build instructions, built executables,
   file hash information, and bills of materials. To successfully accomplish this task, the development team should leverage a robust artifact repository

**Task PS.3.2**

Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials [SBOM]).

**Key Objectives:**

This task has two key objectives:

1. **The preservation of component provenance in support of future analysis and maintenance activities.**

..

   **Analysis:**

   The objective of this task is to record information about all incorporated components (e.g., open-source, commercial, or third-party-developed code) included
   with the software. To accomplish this, the development team should create and maintain a Software Bill of Materials (SBOM), which is a machine-readable
   document that captures information about the software it represents. Information is gathered throughout the entire Software Development Life Cycle (SDLC) and
   includes requirements, licenses, source locations, and known vulnerabilities. All this information is packaged into a single file to enable automated
   analysis.

   For this task, an SBOM should list each component along with information about where and when it was obtained.

2. **The availability of component provenance in support of future analysis and maintenance activities.**

..

   **Analysis:**

   The objective of this task is to present provenance information to the downstream users of the software so they can use it in their risk assessment
   activities. The raw SBOM file should be stored in the source code repository and delivered as part of the release of the software.

   Users of the software should use SBOM to drive the assessment of external components and flag any that have released a newer version, to determine if any new
   vulnerability has been discovered and made public, and to identify components that are no longer maintained or are abandoned. They should also feed
   information about external components into their intrusion detection system to enable real-time monitoring of traffic that may be targeting one of those
   components.

C.3. Produce Well-Secured Software (PW)
---------------------------------------

C.3.1. PRACTICE (PW.1) - Design Software to Meet Security Requirements and Mitigate Security Risks:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify and evaluate the security requirements for the software; determine what security risks the software is likely to face during operation and how the
software’s design and architecture should mitigate those risks; and justify any cases for which risk-based analysis indicates that security requirements should
be relaxed or waived. Addressing security requirements and risks during software design (i.e., secure by design) is key to improving software security and also
helps improve development efficiency.

**Task PW.1.1**

Use forms of risk modeling (e.g., threat modeling, attack modeling, attack surface mapping) to help assess the security risk for the software.

**Key Objectives:**

This task has one key objective:

1. **The identification of cybersecurity risks that the software faces.**

..

   **Analysis:**

   The objective of this task is to understand and document cybersecurity risks specific to the software, thereby enabling protections to be devised and
   incorporated into the design. NIST defines a cybersecurity risk as the loss of confidentiality, integrity, or availability of information, data, or controls,
   with potential adverse impacts on the user of the software. To accomplish this task, the development team should repeatedly perform a variety of risk
   modeling activities. Each activity approaches the task from a different perspective and offers complementary insight into the risks that the software faces.

   Threat modeling starts internally with the software and identifies what needs to be protected. From there, it looks at potential threats to those things.
   Threats are defined as actions or events that result in undesired consequences, specifically the loss of confidentiality, integrity, or availability. The
   Microsoft STRIDE model defines six categories of threats: spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of
   privilege.

   Attack modeling takes the attacker's viewpoint and examines what could be accomplished given a specific (real or theoretical) vulnerability. It examines the
   tactics, techniques, and procedures (TTPs) used by an attacker and the conditions required for each to succeed. Each TTP is then simulated to determine the
   likelihood of success given the current design of the software.

   Attack surface mapping attempts to identify the places in the software that an attacker can interact with. Examples include file input, open ports,
   environment variables, network connections, and human operators. These become the entry points for an attack and are used in both threat and attack modeling
   exercises to establish what might be possible.

   The outcome of this task should be a continuously updated collection of cybersecurity risks applicable to the software and the potential protection
   mechanisms that could be leveraged to mitigate them. This collection should be documented and stored within the development team’s threat modeling system. By
   understanding the potential risks, the development team will be better positioned to add specific design features to mitigate their impact.

**Task PW.1.2**

Track and maintain the software’s security requirements, risks, and design decisions.

**Key Objectives:**

This task has one key objective:

1. **The preservation of design decisions made to mitigate cybersecurity risks.**

..

   **Analysis:**

   The objective of this task is to maintain a record of the security-related software design decisions that have been made and how these decisions satisfy the
   security requirements (see PO.1.2) and mitigate the identified cybersecurity risks (see PW.1.1). Such a record is helpful when analyzing the software’s
   compliance with the stated requirements, and in support of future discussions about new issues, specifically about how a mitigation performed and if it
   should be changed or replaced.

   To successfully meet this objective, the development team should use a risk management system to capture every decision that has shaped the software's
   design.

   A part of this is recording the related design choices for meeting each security requirement and relating this to specific risks that are mitigated because
   of it. If a particular security requirement cannot be met, this fact should also be recorded. The development team should restate what was required and
   explain why they are unable to implement the mitigation. If an alternative mitigation was implemented, then recording details about the alternative is
   critically important.

   Another aspect of this task is documenting any other design choices that have been made beyond the security requirements in an attempt to mitigate other
   identified software-specific risks.

   The outcome associated with meeting this objective is the capture of the complete history of design decisions in the risk management system, which is
   available to support future analysis activities. Each decision should be documented within an Architectural Decision Record (ADR) and stored alongside the
   codebase with other documentation, typically in a “doc/adr” directory. This task supports the reviews performed as part of PW.2.1 by providing the
   development team’s point of view and opinions relative to the security requirements and risks.

**Task PW.1.3**

Where appropriate, build in support for using standardized security features and services (e.g., enabling software to integrate with existing log management,
identity management, access control, and vulnerability management systems) instead of creating proprietary implementations of security features and services.

**Key Objectives:**

This task has two key objectives:

1. **The identification of standardized security features and services that should be leveraged.**

..

   **Analysis:**

   The first objective is to identify existing services that can be leveraged and understand the features each provides. The use of standardized / shared
   services enables different applications to work together and provide functionality that might not be available individually.

   A common example surrounds logging, where collecting events across all aspects of the software and making the information available in a shared manner
   enables complex analysis of events, and the eventual connection of seemingly disjoint actions that ultimately are related. By leveraging a standard logging
   format and using a shared logging service, the software can realize these benefits.

   Another example is authentication, where effectiveness is often tied to the level of rigor needed. Using a feature such as multi-factor authentication can be
   difficult to get right the first time, and reusing existing, proven services is recommended. Additionally, using the same authentication service across
   multiple software products can improve the user’s overall experience by fostering familiarity and understanding.

   To achieve this objective, the development team should establish a list of standardized features and services that are available. Included in this should be
   information about what each service offers and what is required by the software attempting to leverage it. This list should be stored alongside the codebase
   with other documentation. This development team should then use this list as part of the second objective to determine the most effective design for the
   software.

2. **The adoption of designs that leverage existing standardized security features and services.**

..

   **Analysis:**

   The second objective is to encourage designs that leverage the standardized security features and services that were identified as part of the first
   objective. This should become part of the culture within the software development team, with the use of these services being prioritized.

   Successfully achieving this objective entails services being properly integrated and configured for their intended use.

C.3.2. PRACTICE (PW.2) - Review the Software Design to Verify Compliance with Security Requirements and Risk Information:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help ensure the software meets the security requirements and satisfactorily addresses the identified risk information.

**Task PW.2.1**

Have 1) a qualified person (or people) who were not involved with the design and/or 2) automated processes instantiated in the toolchain review the software
design to confirm and enforce that it meets all of the security requirements and satisfactorily addresses the identified risk information.

**Key Objectives:**

This task has two key objectives:

1. **The verification that the software design meets security requirements and mitigates cybersecurity risks.**

..

   **Analysis:**

   The first objective of this task is to verify that the software design properly satisfies the security requirements and addresses the identified risks.
   Security requirements should have been initially established as part of PO.1.1, risks to the software should have been documented as part of PW.1.1, and a
   design should have been documented as part of PW.1.2.

   To achieve this objective, the development team should secure an unbiased expert (e.g., an internal or external review team not involved with the software
   design team) to review design decisions and their impact on each security requirement and cybersecurity risk.

   The outcome of meeting this objective is a report that presents evidence and states an opinion on the software’s mitigation of identified risks. This report
   should be stored alongside the codebase with other documentation.

2. **The revision of an unsatisfactory software design before it advances to implementation.**

..

   **Analysis:**

   The second objective of this task is to keep software in the design phase until it satisfactorily addresses identified risks. Once software advances to
   implementation, changes to the design become more expensive. The development team should look to return an incomplete design to the design team to improve.

   To successfully meet this objective, control gates should be in place that assess proposed designs. These control gates can include manual or automated
   tests, but in both cases, the tests should attempt to identify any security requirement that has not been met. Using the report generated in the meeting, the
   first objective of this task would be one option.

   The outcome of meeting this objective is software that advances to implementation only after its design has been confirmed appropriate.

   Note: Verify Third-Party Software Complies with Security Requirements (PW.3) is moved to PW.4.

C.3.4. PRACTICE (PW.4) - Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lower the costs of software development, expedite software development, and decrease the likelihood of introducing additional security vulnerabilities into the
software by reusing software modules and services that have already had their security posture checked. This is particularly important for software that
implements security functionality, such as cryptographic modules and protocols.

**Task PW.4.1**

Acquire and maintain well-secured software components (e.g., software libraries, modules, middleware, frameworks) from commercial, open-source, and other
third-party developers for use by the organization’s software.

**Key Objectives:**

This task has three key objectives:

1. **The acquisition of trusted external software components.**

..

   **Analysis:**

   The first objective of this task is that only well-secured and trusted external software components are included in the software being developed. Un-trusted
   components increase the risk that malicious functionality is embedded within the component, or that latent vulnerabilities are present due to poor secure
   coding practices.

   To achieve this objective, the development team should perform a variety of data gathering and analysis efforts. They should understand and examine the
   provenance of the component. Organizations might want to consider attestation quality, build transparency, release signing practices, and evidence that
   components were produced using secure development processes. They should analyze the component’s executable code for problems and unexpected functionality.
   They should look into the organizations that developed and maintain the component, and those that provide it to the market, and create a measure of trust for
   those organizations. And the development team should use integrity verification methods to make sure that the component hasn’t been tampered with.

   This task focuses on acquiring and including libraries, frameworks, and dependencies for the software, whereas task PW.1.3 focuses on compliance,
   integration, and use of external services.

2. **The availability of trusted and approved libraries/modules that can be reused by the software being developed.**

..

   **Analysis:**

   The second objective is to establish a collection of approved libraries (internal and external) that the software can leverage to fulfill certain security
   requirements. Ideally, this collection is already available and provided by the organization, but if not, then the development team should determine the
   types of libraries needed, identify appropriate ones, and collect them for later reuse.

3. **The reuse of existing organizationally approved software components.**

..

   **Analysis:**

   The third objective of this task is the integration of the approved software components by the development team during implementation. A well-established
   best practice is to avoid developing one’s own security feature when existing alternatives are already available. Existing components are more likely to have
   initial bugs already found and fixed, and have a proven track record to show their viability.

**Task PW.4.2**

Create and maintain well-secured software components in-house following SDLC processes to meet common internal software development needs that cannot be better
met by third-party software components.

**Key Objectives:**

This task has one key objective:

1. **The availability of needed, well-secured, internally developed software components.**

..

   **Analysis:**

   The objective of this task is to properly respond to the lack of an appropriate external software component. The primary desire is to acquire and reuse
   well-secured external components, but when such components are not available, the development team is forced to develop its own.

   To achieve this objective, the development should first determine which components are not available externally. Once a list of needed components is
   established, the development team should follow the same secure coding practices that are in place for the primary software product being developed. (see
   task PW.5.1)

**Task PW.4.4**

Verify that acquired commercial, open-source, and all other third-party software components comply with the requirements, as defined by the organization,
throughout their life cycles.

**Key Objectives:**

This task has one key objective:

1. **The continuous trust in external software components used by the software.**

..

   **Analysis:**

   The objective of this task is the ongoing monitoring and updating of all external components being used by the software. To achieve this objective, the
   development team should establish a continuous check of all known components in use. Common things to look at are the component version, whether a more
   recent version exists, known vulnerabilities, the organizations and people involved in maintaining the component, and how the component is protected by the
   vendor.

   Successfully meeting this objective requires the development team to create action plans for any component that ends up falling below the desired level of
   acceptability during this ongoing monitoring. The development team should act quickly to respond to changes in the component and make sure the most
   appropriate version is being leveraged.

C.3.5. PRACTICE (PW.5) - Create Source Code by Adhering to Secure Coding Practices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decrease the number of security vulnerabilities in the software, and reduce costs by minimizing vulnerabilities introduced during source code creation that meet
or exceed organization-defined vulnerability severity criteria.

**Task PW.5.1**

Follow all secure coding practices that are appropriate to the development languages and environment to meet the organization’s requirements.

**Key Objectives:**

This task has one key objective:

1. **The elimination of security-related weaknesses in the code.**

..

   **Analysis:**

   The objective of this task is to eliminate weaknesses in the source code. A weakness is a mistake made by the developer during the design or implementation
   of the code that, under certain circumstances, could lead to vulnerabilities.

   As part of this task, the development team should select or create a secure coding standard that specifies appropriate secure coding practices and provides
   guidance for implementing the practices.

   In addition to following secure coding guidance, the development team should perform a variety of analyses to identify mistakes that inevitably occur. Some
   recommended activities are ongoing training, use of static analysis tools, peer review, and dynamic testing. All these activities should leverage the secure
   coding guidance as a foundation for the types of issues to prevent.

   To successfully meet this objective, the development team should be trained on the secure coding standard, follow it during implementation, and present the
   results of the code analysis.

C.3.6. PRACTICE (PW.6) - Configure the Compilation, Interpreter, and Build Processes to Improve Executable Security:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decrease the number of security vulnerabilities in the software and reduce costs by eliminating vulnerabilities before testing occurs.

**Task PW.6.1**

Use compiler, interpreter, and build tools that offer features to improve the security of executables.

**Key Objectives:**

This task has one key objective:

1. **The selection of tools that offer protections to improve executable security.**

..

   **Analysis:**

   The objective of this task is to eliminate or mitigate vulnerabilities in the software before it is released. Many compilers and build tools can add
   protections into the code to guard against common types of attacks. By mitigating attacks, mistakes/weaknesses made by the development team are rendered
   non-exploitable and hence are not vulnerabilities.

   To achieve this objective, the development team should research available tools and select those that provide such features. Enabling specific features is
   covered in Task PW.6.2.

**Task PW.6.2**

Determine which compiler, interpreter, and build tool features should be used and how each should be configured, then implement and use the approved
configurations.

**Key Objectives:**

This task has two key objectives:

1. **The elimination of vulnerabilities in the executable code.**

..

   **Analysis:**

   The objective of this task is to enable approved security features in the tools used to compile and build the software and thus eliminate or mitigate
   vulnerabilities before the software is released.

   To accomplish this objective, the development team should keep a list of the features being leveraged.

2. **The repeatability of tool configurations aimed at code security thus increasing the likelihood that software is as secure as possible.**

..

   **Analysis:**

   The objective of this task is to ensure that security-focused features included in the tools used by the development team are enabled. Automating the
   configuration of these tools through concepts such as configuration-as-code helps add consistency across tool updates and environment shifts.

   To accomplish this objective, the development team should verify that the chosen features are consistently enabled across tool updates.

C.3.7. PRACTICE (PW.7) - Review and/or Analyze Human-Readable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help identify vulnerabilities so that they can be corrected before the software is released to prevent exploitation. Using automated methods lowers the effort
and resources needed to detect vulnerabilities. Human-readable code includes source code, scripts, and any other form of code that an organization deems
human-readable.

**Task PW.7.1**

Determine whether code review (a person looks directly at the code to find issues) and/or code analysis (tools are used to find issues in code, either in a
fully automated way or in conjunction with a person) should be used, as defined by the organization.

**Key Objectives:**

This task has one key objective:

1. **The selection of appropriate static analysis technique(s) to identify issues in the code.**

..

   **Analysis:**

   The objective of this task is to choose the static analysis technique(s) that would be the most effective for the software project. Static analysis is the
   examination of the source code without any execution of the code. (Analysis via execution is known as dynamic analysis) There are two primary methods of
   static analysis.

   The first is known as manual code review, where a human reads each line of code and attempts to identify mistakes made by the developer. This technique has
   the benefit of being very broad in the types of issues that could be found, as humans can comprehend a large variety of issues. The disadvantage is the speed
   at which such a review can take place.

   The second technique uses tools to analyze the source code in an automated way. The tools often create a model of the code and then look for patterns that
   expose the presence of certain types of issues. The advantage of this technique is the speed and volume of code that can be analyzed. The disadvantage is
   that tools are often limited in the types of issues that they can see in the patterns.

   Manual and automated techniques can also be combined, in which a human uses the tools' output to focus their inspection.

**Task PW.7.2**

Perform the code review and/or code analysis based on the organization’s secure coding standards, and record and triage all discovered issues and recommended
remediations in the development team’s workflow or issue-tracking system.

**Key Objectives:**

This task has one key objective:

1. **The identification of issues in the software that need to be corrected.**

..

   **Analysis:**

   The objective of this task is to identify issues in the software that need to be corrected. To achieve this objective, the development team should perform
   the static analysis techniques that were deemed appropriate in PW.7.1 for this development effort.

   The development team should have a secure coding standard as part of task PW.5.1that identifies the secure coding practice that should be followed. The
   static analysis being performed should focus on identifying places of non-compliance with these practices.

   Additionally, successfully meeting this objective requires the development team to properly assess and record all issues identified by static analysis. This
   enables progress on fixing the issues to be tracked, thus making sure issues aren’t lost or forgotten about.

C.3.8. PRACTICE (PW.8) - Test Executable Code to Identify Vulnerabilities and Verify Compliance with Security Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help identify vulnerabilities so that they can be corrected before the software is released in order to prevent exploitation. Using automated methods lowers the
effort and resources needed to detect vulnerabilities and improves traceability and repeatability. Executable code includes binaries, directly executed
bytecode, source code, and any other form of code that an organization deems executable.

**Task PW.8.1**

Determine whether executable code testing should be performed to find vulnerabilities not identified by previous reviews, analysis, or testing, and, if so,
which types of testing should be used.

**Key Objectives:**

This task has one key objective:

1. **The selection of appropriate dynamic analysis technique(s) to identify issues in the code.**

..

   **Analysis:**

   The objective of this task is to determine if dynamic analysis techniques are appropriate for the software being developed and then to choose the
   technique(s) that would be the most effective. Dynamic analysis is performed by executing the software and monitoring the changes to the system that result.
   (Analysis of just the code without execution is known as static analysis)

   Dynamic analysis can be challenging to implement and may not be easy to implement for all types of software. In its simplest form, dynamic analysis consists
   of a collection of predetermined test cases that attempt to execute critical paths through the software using inputs that are known to be dangerous or
   incorrect. If a vulnerability exists in the software, then these inputs will exercise it and produce unexpected results (e.g., a system crash or information
   exposure). Because of this danger, development teams should avoid performing dynamic analysis on live systems and instead set up test environments that mimic
   the operational environment.

   Fuzz testing is another popular type of dynamic testing and involves repeatedly sending random and unexpected data, along with specially crafted data to test
   edge conditions, to the software via its input channels. By monitoring how the software responds to this often invalid data, the developer can identify a
   weakness and fix the software to more appropriately handle the input that triggered it.

**Task PW.8.2**

Scope the testing, design the tests, perform the testing, and document the results, including recording and triaging all discovered issues and recommended
remediations in the development team’s workflow or issue tracking system.

**Key Objectives:**

This task has one key objective:

1. **The identification of issues in the software that need to be corrected.**

..

   **Analysis:**

   The objective of this task is to identify issues in the software that need to be corrected. To achieve this objective, the development team should perform
   the dynamic analysis techniques that were deemed appropriate in PW.8.1 for this development effort.

   Successfully meeting this objective means that the development team should properly assess and record all issues that the dynamic analysis identifies. This
   enables progress on fixing the issues to be tracked, thus making sure issues aren’t lost or forgotten about.

C.3.9. PRACTICE (PW.9) - Configure Software to Have Secure Settings by Default:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help improve the security of the software at the time of installation to reduce the likelihood of the software being deployed with weak security settings,
putting it at greater risk of compromise.

**Task PW.9.1**

Define a secure baseline by determining how to configure each setting that has an effect on security or a security-related setting so that the default settings
are secure and do not weaken the security functions provided by the platform, network infrastructure, or services.

**Key Objectives:**

This task has one key objective:

1. **Establishing a secure baseline configuration for the software.**

..

   **Analysis:**

   The objective of this task is to determine the most secure configuration for the software and then make that the default.

   To achieve this objective, the development team should examine each possible configuration setting and select default values that best protect
   confidentiality, integrity, and availability. The actual
   implementation of these configuration settings is covered in Task PW.9.2.

**Task PW.9.2**

Implement the default settings (or groups of default settings, if applicable), and document each setting for software administrators.

**Key Objectives:**

This task has two key objectives:

1. **Configuring the software to be as secure as possible.**

..

   **Analysis:**

   The objective of this task is to configure the software in the most secure state possible. To accomplish this, the development team should attempt to keep
   the default settings and only change them if there is a legitimate need.

2. **Verifying that the software is configured as securely as possible.**

..

   **Analysis:**

   The objective of this task is to be able to show that the software is configured in its most secure state. To accomplish this, the development team should
   document each relevant setting and record the actual value relative to the default value along with any reason for divergence.

C.4. Respond to Vulnerabilities (RV)
------------------------------------

C.4.1. PRACTICE (RV.1) - Identify and Confirm Vulnerabilities on an Ongoing Basis:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help ensure that vulnerabilities are identified more quickly so that they can be remediated more quickly in accordance with risk, reducing the window of
opportunity for attackers.

**Task RV.1.1**

Gather information from software acquirers, users, and public sources on potential vulnerabilities in the software and third-party components that the software
uses, and investigate all credible reports.

**Key Objectives:**

This task has one key objective:

1. **The identification of known vulnerable software components in use by the software.**

..

   **Analysis:**

   The objective of this task is to quickly identify publicly disclosed vulnerabilities in any software being developed or maintained by continuously monitoring
   public vulnerability sources, such as the National Vulnerability Database (https://nvd.nist.gov) and the Open-Source Vulnerability (OSV) database
   (https://osv.dev).

   To successfully meet this objective, development teams should establish an activity within their lifecycle to review all potentially relevant reports,
   confirm applicability, and enforce action to mitigate the issues.

   Having an accurate SBOM (see task PS.3.2) enables this task to be performed efficiently as tools can pull the list of components from the SBOM and match
   those to reports in known information sources.

**Task RV.1.2**

Review, analyze, and/or test the software’s code and its default and other common configurations to identify or confirm the presence of previously undetected
vulnerabilities.

**Key Objectives:**

This task has two key objectives:

1. **The identification of issues in the software that need to be corrected.**

..

   **Analysis:**

   The first objective of this task is to continuously analyze the software throughout the operational phase of its lifecycle. The type of analysis is similar
   to the analysis that is performed during the implementation and testing phases. The only difference with this task is that it is set up to be performed
   repeatedly. The reason for this is that analysis tools improve, and the issues they can detect change, raising the possibility that previously undetected
   issues may be found.

2. **The identification of more secure configurations that should be made part of the default.**

..

   **Analysis:**

   This task also strives to monitor the default configuration of the software to determine if more secure configurations are possible. To support this task,
   the development team should monitor existing operational instances of the software and known exploits that have been seen. Studying these events can shed
   light on ways to improve the configuration of the software to mitigate similar exploits in the future.

**Task RV.1.3**

Have a policy that addresses vulnerability disclosure and remediation, and implement the roles, responsibilities, and processes needed to support that policy.

**Key Objectives:**

This task has one key objective:

1. **The responsible disclosure of issues in the software.**

..

   **Analysis:**

   The objective of this task is to promote the responsible disclosure of discovered issues in the software. Ideally, all discovered issues will be reported to
   the development team before being publicly released. This gives the development team an opportunity to fix the issue and push an update to users of the
   software before external actors learn about the issue and use it to exploit the software.

   To successfully achieve this objective, the development team should create and publish a policy for how vulnerabilities discovered in the software should be
   disclosed and the timeline for such a disclosure. The development team should also establish a dedicated team to promptly review all submitted disclosures
   and respond to each in a timely fashion.

C.4.2. PRACTICE (RV.2) - Assess, Prioritize, and Remediate Vulnerabilities:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help ensure that vulnerabilities are remediated in accordance with risk to reduce the window of opportunity for attackers.

**Task RV.2.1**

Analyze each vulnerability to gather sufficient information about risk and plan its remediation or other risk response.

**Key Objectives:**

This task has one key objective:

1. **The confirmation and prioritization of issues reported in the software.**

..

   **Analysis:**

   The objective of this task is to determine which issues should be fixed first. The ideal situation is that all issues are fixed immediately, but the reality
   is that fixes can take time to implement and test. If multiple issues are reported within a given timeframe, choices must be made about which issue to work
   on first. A triage process should be defined by the development team, and disclosed vulnerabilities should be analyzed to determine their priority relative
   to other outstanding issues.

**Task RV.2.2**

Plan and implement risk responses for vulnerabilities.

**Key Objectives:**

This task has one key objective:

1. **The timely resolution of issues in the software.**

..

   **Analysis:**

   The objective of this task is to mitigate any disclosed vulnerability as quickly as possible. Tasks RV.1.1 and RV.1.2 are where the disclosures will come
   from. As issues are discovered, a ticket should be created in the issue tracking tool and the development team should be tasked with implementing a fix.

C.4.3. PRACTICE (RV.3) - Analyze Vulnerabilities to Identify Their Root Causes:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help reduce the frequency of vulnerabilities in the future.

**Task RV.3.1**

Analyze identified vulnerabilities to determine their root causes.

**Key Objectives:**

This task has one key objective:

1. **The understanding of common root causes in support of future training and analysis efforts.**

..

   **Analysis:**

   The objective of this task is to better understand the root causes of vulnerabilities that have been discovered within the software. This understanding
   should then be leveraged by task RV.3.2 to improve future development practices.

   To successfully achieve this objective, the development team should establish a tracking solution to record each vulnerability and its root cause, and
   incentivize developers to consistently use the system.

**Task RV.3.2**

Analyze the root causes over time to identify patterns, such as a particular secure coding practice not being followed consistently.

**Key Objectives:**

This task has two key objectives:

1. **The continuous improvement of developer training.**

..

   **Analysis:**

   The first objective of this task is to use the knowledge of which root causes have been leading to issues in the software to improve the training that is
   given to the development staff. The presence of an issue often means that the underlying root cause is not fully understood by the developer, or the existing
   training doesn’t address it at all. Improvements in the training should result in a reduction in future issues being made.

2. **The improvement of software testing.**

..

   **Analysis:**

   The second objective of this task is to improve the software testing techniques to cover the types of root causes that are being seen. Adding tests to
   identify these specific types of weaknesses should reduce the number of issues making it into production.

**Task RV.3.3**

Review software for similar vulnerabilities to eradicate a class of vulnerabilities and proactively remediate them rather than waiting for external reports.

**Key Objectives:**

This task has one key objective:

1. **The identification of issues in the software that need to be corrected.**

..

   **Analysis:**

   The objective of this task is to identify previously undetected issues in the software by using the root cause analysis performed in task RV-3.1 to search
   for similar issues elsewhere in the code. When a weakness exists in the code, it is often due to training and/or testing techniques that don’t cover that
   specific type of issue. The lack of coverage for a weakness increases the chances that the issue will exist in multiple places.

**Task RV.3.4**

Review the SDLC process and update it, if appropriate, to prevent (or reduce the likelihood of) the root cause recurring in software updates or in newly created
software.

**Key Objectives:**

This task has one key objective:

1. **The improvement of development practices throughout the SDLC.**

..

   **Analysis:**

   The objective of this task is to use the knowledge of issues that have been found to improve the overall development practices for future revisions. By
   constantly improving the processes that the development team follows less mistakes should be made.
