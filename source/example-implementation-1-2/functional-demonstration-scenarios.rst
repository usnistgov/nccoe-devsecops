Functional Demonstration Scenarios
==================================

This section details the scenarios that the NCCoE project team used to demonstrate activities to perform during each of the SDLC phases. These scenarios
were derived from the descriptions and components shown in the Notional Reference Model section for each phase of the DevSecOps lifecycle. Each scenario
includes:

1. Objective: Outlines what the demonstration scenario intends to achieve.

2. A table with the following columns:

   - Scenario ID: used to map the results in the Functional Demonstration Results section.

   - Demonstration Step: Each demonstration step covers a specific activity or activities to complete the scenario.

   - Component(s): A list of components is identified for each demonstration step that should be used.

   - Expected Outcome: The outcome of the demonstration required to consider a successful activity.

   - SSDF Task: The SSDF practice and task number associated with the activity. The presented mapping represents the SSDF task(s) that the Demonstration Step helps achieve.

Note: The current AI scenarios for each phase focus primarily on Generative AI. The Agentic AI demonstrations are planned for future publication, and the AI
components section will be updated to reflect these additions.

.. _scenario-plan:

Phase A - Plan
~~~~~~~~~~~~~~

Teams define functional and security requirements, establish secure practices, and create roadmaps, updating them as feedback from later phases informs new
functional or security needs.


.. _scenario-a-1:

Scenario A-1: Team Collaboration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Enable teams to discuss, document, and plan product designs, feature prioritizations, task assignments, and responses to security
vulnerabilities, threats, and software issues.

.. list-table::
   :header-rows: 1
   :widths: 19 32 27 53 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-1.1
     - Implement systems and tools to allow stakeholders to collaborate and document information such as requirements, tasks, etc.
     - Project Management System; Requirements Management System; Team Collaboration Tools; Ticketing System
     - Users have access to the project plan, workflows, and assigned tasks.
     - N/A
   * - A-1.2
     - Provision and delegate project roles to allow specific organizational functions (e.g., development, security, and operational).
     - Project Management System; Requirements Management System; Ticketing System
     - Users are granted access to specific role-based functions which allow required actions and responsibilities to be assumed and executed.
     - PO.2.1


.. _scenario-a-2:

Scenario A-2: Requirements Collection and Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure teams derive requirements to identify, document, and prioritize work to implement them after initial planning.

.. list-table::
   :header-rows: 1
   :widths: 18 45 30 39 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-2.1
     - Develop, record, and maintain requirements for the sample software application as well as infrastructure.
     - Requirements Management System
     - Requirements are created documented and maintained in the system.
     - PW.1.2
   * - A-2.2
     - Assign requirements to stakeholders responsible for developing the requirements.
     - Requirements Management System; Ticketing System
     - Stakeholders receive assignments.
     - N/A


.. _scenario-a-3:

Scenario A-3: Product Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** A secure and functional design that implements the requirements of software applications.

.. list-table::
   :header-rows: 1
   :widths: 19 44 32 44 21

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-3.1
     - Teams create secure designs for software applications producing artifacts (e.g., architecture, diagrams, and technical specifications) as necessary.
     - Product Management System
     - Designs are created that mitigate as much risk as possible.
     - | PW.1.2
       | PW.1.3
   * - A-3.2
     - Track and update functional and security tasks for software applications including the creation, assignment, and resolution of tasks.
     - Requirements Management System; Ticketing System
     - Tickets are updated based on tasks. Requirements are documented in the Requirements Management System and tickets are created or updated based on
       required tasking.
     - N/A
   * - A-3.3
     - Document product design and related artifacts (e.g., product vision or roadmaps, features, and growth strategy).
     - Product Management System
     - Product design and necessary changes to product vision, roadmaps, features, and grow strategy are documented accordingly to track product and component
       changes.
     - PW.1.2


.. _scenario-a-4:

Scenario A-4: Bug, Defect, and Issue Tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Establishment of an issue tracking system that enables the documentation of discovered issues (e.g., performance problems, security
vulnerabilities, and application defects) within the software applications, CI/CD pipelines, environments, or operational systems. In the plan phase, initial
bugs and defects may be identified through requirements and design analysis. Continue to create, track, and resolve tickets as bugs and defects are identified
throughout the SDLC.

.. list-table::
   :header-rows: 1
   :widths: 18 45 28 45 24

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-4.1
     - Document issues discovered in all phases.
     - Ticketing System
     - High level and technical issues are documented by creating tickets.
     - PW.7.2
   * - A-4.2
     - Assign the tickets related to each issue to relevant team members.
     - Ticketing System
     - All issues are tracked via tickets and are assigned to the appropriate team member.
     - PW.7.2


.. _scenario-a-5:

Scenario A-5: Risk Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Teams assess the risk of known vulnerabilities and monitor application and system impacts over time.

.. list-table::
   :header-rows: 1
   :widths: 18 43 31 45 24

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-5.1
     - Identify risks (organizational, system, or application level) for the sample software application and infrastructure based on the requirements produced.
     - Risk Management System
     - Risks are identified and documented.
     - PW.1.1
   * - A-5.2
     - Develop and prioritize risk mitigation solutions for the risks identified.
     - Risk Management System; Ticketing System
     - Tickets are created and updated based on new risks. Mitigations and solutions are documented in tickets as risks are resolved.
     - PW.1.2


.. _scenario-a-6:

Scenario A-6: Threat Modeling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** During the planning phase, teams identify and assess new and ongoing security threats to software applications and systems and establish a
process for continuous monitoring.

.. list-table::
   :header-rows: 1
   :widths: 18 43 30 42 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-6.1
     - Review independently verified cyber intelligence, threat actors or campaigns, software vulnerabilities, and other security relevant information.
     - Cyber Intelligence, Threat, and Security Metadata Feeds; Ticketing System
     - Results of cyber intelligence and other security feeds are reviewed and documented. Tickets are created and updated to track and resolve issues related
       to threats.
     - PW.1.1
   * - A-6.2
     - Leverage a threat modeling tool to create a sample mockup of the software application's architecture, including key components (e.g., software
       components, databases, third-party tools, third-party services), data flows, trust boundaries, and system actors.
     - Threat Modeling System
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - PW.1.1
   * - A-6.3
     - Perform threat modeling exercises to examine reviewed cyber intelligence, threat actors, campaigns, software vulnerabilities or other security relevant
       information against potential training scenarios created from previously reviewed information or theoretical scenarios.
     - Cyber Intelligence, Threat, and Security Metadata Feeds; Threat Modeling System
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - PW.1.1


.. _scenario-a-7:

Scenario A-7: Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Teams create, update, manage, and evaluate systems, applications, and support software component configurations. Outputs and information from
previous scenarios are leveraged for configuration management.

.. list-table::
   :header-rows: 1
   :widths: 18 43 30 42 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-7.1
     - Use a configuration management tool to manage changes, track version control, and automate commit hooks to check code.
     - Configuration Management System; SCM System
     - Configurations are created and updated.
     - PS.1.1
   * - A-7.2
     - Track configuration baselines and changes based on documented requirements that are captured in Ticketing or Requirements Management Systems.
     - Requirements Management System; Ticketing System
     - Tickets are created and updated as configurations change. Requirements Management Systems are updated to track configuration changes over time.
     - N/A


.. _scenario-a-8:

Scenario A-8: Certificates, Credentials, and Secrets Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Identify and establish policies for all certificates, credentials, and secrets to include ownership, usage, lifecycle functions (e.g., issuance,
rotation, and revocation), and secure storage mechanisms.

.. list-table::
   :header-rows: 1
   :widths: 18 43 30 42 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-8.1
     - Develop policies for certificates, credentials, and secrets to protect systems and software application.
     - Certificate Management System; Credential Management System; Secrets Management System
     - Policies are defined and implemented in certificate, credential, and secret management systems.
     - PW.1.2
   * - A-8.2
     - Test and validate the systems are functioning properly.
     - Certificate Management System; Credential Management System; Secrets Management System
     - Certificates, credentials, and secrets are scanned or tested to verify access and policy configurations.
     - PW.2.1
   * - A-8.3
     - Review and remediate that certificates, credentials, and secrets that have been identified as disclosed or are susceptible to attack.
     - Certificate Management; System; Credential Management System; Secrets Management System
     - Certificates, credentials, and secrets are verified as safe to use and are rotated, revoked, or reissued in the event of disclosure or potential
       vulnerability.
     - PW.2.1


.. _scenario-a-9:

Scenario A-9: CI/CD Pipeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Develop CI/CD pipelines and automated components. Results are reviewed to provide input for components throughout the Plan phase.

.. list-table::
   :header-rows: 1
   :widths: 18 40 33 41 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-9.1
     - Prepare the automation environment by identifying the pipeline definitions, configurations, tools, IaC, and source code.
     - CI/CD Pipelines; Configuration Management System
     - CI/CD Pipelines are created, updated, and maintained successfully so automated actions can be performed as required.
     - | PO.3.1
       | PO.3.2
       | PO.3.3
   * - A-9.2
     - Define and automate configurations, IaC, and source code.
     - CI/CD Pipelines; Configuration Management System; SCM System
     - Configurations, IaC, and source code are obtained by CI/CD Pipelines and are used as part of the build process.
     - | PO.3.1
       | PO.3.2
       | PO.3.3
   * - A-9.3
     - Validate pipeline definitions against design requirements.
     - CI/CD Pipelines; Requirements Management System
     - Requirements and designs are verified and logged by CI/CD Pipelines.
     - | PO.3.1
       | PO.3.2
       | PO.3.3


.. _scenario-a-10:

Scenario A-10: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure zero trust (ZT) policies are developed in the Plan phase. All principles and policies should be documented and have audit trails.

.. list-table::
   :header-rows: 1
   :widths: 18 40 33 41 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-10.1
     - Develop and apply policies in ZT solution tools to provide authorized users access to systems and tools that manage the development of the software
       applications.
     - ZT Security System
     - User access to systems (e.g., Ticketing) is allowed or denied based on ZT policies.
     - PO.5.2
   * - A-10.2
     - Develop and apply policies to securely store and encrypt documents such as requirements and design documents.
     - ZT Security System
     - Requirement and design documents are protected and stored. Only authorized personnel can access and distribute them.
     - PO.5.1
   * - A-10.3
     - Develop and apply policies in ZT solution tools to provide secure system-to-system communication.
     - Certificate Management System; ZT Security System
     - Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices,
       including rotation and short expiration times.
     - PO.5.1


.. _scenario-a-11:

Scenario A-11: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components allow teams to analyze, generate, augment, or automate the generation and management of requirements, work items, tickets, or
issues. Project, product, and requirements management systems can utilize generated summaries or reports to manage projects and products throughout the SDLC. AI
can help generate new product designs or features, resolve defects and vulnerabilities, or assist with source code management (SCM) activities. Configuration,
credential, and secret management systems can then leverage the generated analysis of artifacts to remediate discovered risks, threats, and vulnerabilities.

.. list-table::
   :header-rows: 1
   :widths: 18 40 33 41 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - A-11.1
     - Analyzes requirements and creates new work items, tickets, or issues.
     - AI Components; Project Management System; Requirements Management System; Ticketing System
     - New work items, tickets, or issues are generated.
     - | PW.1.1
       | PW.1.2
   * - A-11.2
     - Groups work items, tickets, or issues into epics or user stories.
     - AI Components; Ticketing System
     - Existing work items, tickets, or issues are assigned to epics or user stories.
     - N/A
   * - A-11.3
     - Detects duplicate work items, tickets, or issues.
     - AI Components; Ticketing System
     - Duplicate work items, tickets, or issues are marked as closed or removed.
     - N/A
   * - A-11.4
     - Validates requirements against known standards and frameworks.
     - AI Components; Project Management System; Requirements Management System; Risk Management System
     - Standards or framework compliance requirements are documented for project, requirements, or risk management systems.
     - PW.1.3
   * - A-11.5
     - Summarizes discussions, shared documents, source code, or other artifacts.
     - AI Components; Project Management System; Requirements Management System; Ticketing System
     - Summaries are documented in project or requirements management system.
     - N/A
   * - A-11.6
     - Constructs images, models, or mock-ups based on existing design requirements.
     - AI Components; Product Management System
     - Images, models, or mock-ups are documented in product management system.
     - PW.2.1
   * - A-11.7
     - Identifies resources required to execute product vision, strategy, or roadmaps.
     - AI Components; Project Management System; Product Management System
     - Required resources are identified, documented for project or design management systems.
     - N/A
   * - A-11.8
     - Suggests modification to product vision, strategy, or roadmaps.
     - AI Components; Project Management System
     - Modifications are generated and saved for future use.
     - N/A
   * - A-11.9
     - Provides mitigations for risks, threats, or vulnerabilities based on provided reports or monitoring information.
     - AI Components; Risk Management System; Threat Modeling
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - PW.2.1

.. _scenario-develop:

Phase B – Develop
~~~~~~~~~~~~~~~~~

Teams create and review code, infrastructure, and policies with approved tools to meet requirements and ensure quality, security, and policy concurrence early
in the process.

.. _scenario-b-1:

Scenario B-1: Software Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Developers follow secure coding practices. They use IDEs, Command Line Interface (CLI) tools, software libraries, and AI tools to write source
code, leverage library and software integrations, and automate development activities.

.. list-table::
   :header-rows: 1
   :widths: 18 40 33 41 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-1.1
     - Develop source code, unit tests, and automation scripts.
     - Developer Tools (e.g., IDE, CLI, and Binaries), SCM System
     - Source code, unit tests, and automation scripts are created.
     - PW.5.1
   * - B-1.2
     - Manage and retrieve development artifacts from the repository.
     - Artifact Repository
     - Artifacts are retrieved and managed via a repository.
     - PW.4.4
   * - B-1.3
     - Build and test code prior to commitment.
     - SCM System; Unit Test Framework
     - Code is built and unit tests are run.
     - | PW.6.1
       | PW.6.2

.. _scenario-b-2:

Scenario B-2: Code Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Analyze code using various tools to identify vulnerabilities, errors, compliance, software dependencies, license issues, and sensitive
information.

.. list-table::
   :header-rows: 1
   :widths: 18 40 33 41 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-2.1
     - Analyze source code with a SAST tool.
     - CI/CD Pipeline; SAST System; SCM System
     - Any vulnerabilities are found, and logs are provided.
     - | PW.7.1
       | PW.7.2
   * - B-2.2
     - Analyze the code for code style issues, potential defects, or code standard violations.
     - CI/CD Pipeline; Lint Tool; SCM System
     - Security issues and style problems are found via the linting tool. Logs are provided to the developer.
     - | PW.7.1
       | PW.7.2
   * - B-2.3
     - Analyze third-party libraries for security problems.
     - CI/CD Pipeline; SCA System; SCM System
     - SCA tool runs, vulnerabilities are detected, and logs are provided.
     - PW.4.4
   * - B-2.4
     - Scan for secrets in the code prior to committing.
     - CI/CD Pipeline; Secret Scanner
     - Credentials, Keys, and other sensitive information are detected. Results are provided to developers.
     - | PW.7.1
       | PW.7.2

.. _scenario-b-3:

Scenario B-3: Develop Infrastructure as Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Develop Infrastructure-as-Code (IaC) to create system and application configurations, maintain security baselines, and ensure consistent
implementations in each operating environment.

.. list-table::
   :header-rows: 1
   :widths: 18 34 37 43 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-3.1
     - Develop IaC scripts.
     - Developer Tools (e.g., IDE, CLI, and Binaries); SCM System
     - IaC scripts are created.
     - N/A
   * - B-3.2
     - Scan the IaC scripts for vulnerabilities.
     - CI/CD Pipeline; IaC Scanner; IaC Scripts; SCM System
     - IaC code problems are found and logs provided.
     - N/A

.. _scenario-b-4:

Scenario B-4: Source Code Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Developers use SCM to review source code changes, collaborate with team members, log outstanding issues, and maintain visibility in software
projects. Developers use commit hooks to automatically run checks (e.g., SAST, SCA, and linting) before committing changes to source code. Branch and merge
protections are used to ensure that only secure and approved code is merged into the main codebase.

.. list-table::
   :header-rows: 1
   :widths: 18 34 37 45 25

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-4.1
     - Approved developers are assigned to perform code reviews.
     - SCM System
     - Changes are reviewed by approved developers prior to merging.
     - PS.1.1
   * - B-4.2
     - Create changes to source code.
     - SCM System
     - Code is created by developers and committed to source code repositories.
     - PS.1.1
   * - B-4.3
     - Client-side commit hooks are used to secure code.
     - SAST System; SCA System; Lint Tool; SCM System; Secret Scanner;
     - Code is scanned and is not committed if errors are found.
     - | PO.3.1
       | PO.3.2
       | PW.7.2
   * - B-4.4
     - Enforce branch and merge protection.
     - SCM System
     - Code that has not been approved cannot be merged into main.
     - PW.7.2

.. _scenario-b-5:

Scenario B-5: Securing Sensitive Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Developers use certificates, credentials, and secrets management to store, track, and maintain sensitive assets across their lifecycle to prevent
unauthorized access and disclosure.

.. list-table::
   :header-rows: 1
   :widths: 18 34 37 45 25

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-5.1
     - Store and manage credentials for people and services.
     - Credential Management System
     - Credentials are stored and managed securely.
     - | PO.3.1
       | PO.3.2
   * - B-5.2
     - Leverage a secrets management system to store and manage secrets.
     - Secrets Management System
     - Keys and other secrets are stored and managed securely.
     - | PO.3.1
       | PO.3.2
   * - B-5.3
     - Leverage a certificate management system to store and manage certificates.
     - Certificate Management System
     - Certificates are stored and managed (e.g., issuance, rotation, revocation) securely.
     - | PO.3.1
       | PO.3.2


.. _scenario-b-6:

Scenario B-6: Firmware Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Integrate firmware management tools into the CI/CD pipeline to maintain, update, and secure firmware that is used throughout each phase of the
development lifecycle. It supports initial development, vulnerability scanning, remediation, secure updates, and ongoing monitoring.

.. list-table::
   :header-rows: 1
   :widths: 18 44 26 44 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-6.1
     - Create and manage firmware.
     - Firmware Services
     - Firmware is developed and managed.
     - N/A
   * - B-6.2
     - Use firmware management tools to sign and verify firmware signatures.
     - Firmware Services
     - Signed firmware artifacts are verified and authentic.
     - PS.2.1
   * - B-6.3
     - Log status and findings of firmware changes.
     - Firmware Services
     - Logs of firmware updates or changes are captured.
     - N/A


.. _scenario-b-7:

Scenario B-7 Artifact Signing and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Developers use artifact signing to establish and verify the integrity and authenticity of source code, binaries, and other components. Software
certificates, checksums, or other hashing functions are used for artifacts to help detect unauthorized use or tampering.

.. list-table::
   :header-rows: 1
   :widths: 18 44 26 44 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-7.1
     - Digitally sign the software components (e.g., source code, commits, container images, binaries, and software libraries).
     - Artifact Signing and Verification Tool; Certificate Management System; CI/CD Pipeline; HSM
     - Software components are digitally signed, and secrets are stored and protected by HSM.
     - PS.2.1
   * - B-7.2
     - Verify software components have not been tampered with.
     - Attestation Signing and Verification Tool; CI/CD Pipeline
     - Signed software components are authentic and not tampered with.
     - PS.2.1
   * - B-7.3
     - Log status and findings of the results of integrity verification.
     - CI/CD Pipeline
     - Detailed logging is captured and alerts sent to stakeholders.
     - PS.2.1

.. _scenario-b-8:

Scenario B-8: Cryptographic Key Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Certificates and private keys are maintained (e.g., issuance, storage, rotation, or revocation) to ensure overall source integrity,
authorization, and proper attribution.

.. list-table::
   :header-rows: 1
   :widths: 18 44 26 41 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-8.1
     - Validate that certificates and private keys are properly managed.
     - Certificate Management System
     - Certificates and private keys are stored and managed securely in the Certificate Management System.
     - | PO.3.1
       | PO.3.2
   * - B-8.2
     - Manage credentials and secrets related to certificates.
     - Credential Management System; Secrets Management System
     - Secrets and credentials are securely managed and stored in Secrets Management System.
     - | PO.3.1
       | PO.3.2

.. _scenario-b-9:

Scenario B-9: Develop CI/CD Pipeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Tools are configured, and scripts are written and updated to ensure the CI/CD pipeline is secure and operates as expected. Additionally, a
development pipeline may be created to allow developers to build and test their code before any commits.

.. list-table::
   :header-rows: 1
   :widths: 18 44 26 41 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-9.1
     - Develop pipeline scripts for automation of the pipeline.
     - CI/CD Pipeline; Developer Tools (e.g., CLI and Binaries); Configuration Management System; SCM System
     - Scripts to automate the CI/CD pipeline and build its environments are stored in SCM.
     - | PO.3.1
       | PO.3.2

.. _scenario-b-10:

Scenario B-10: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the zero trust policies created in the Plan phase are implemented in this phase to ensure least privilege, secure access to systems,
software applications, and sensitive resources hosted throughout the Develop Phase environments.

.. list-table::
   :header-rows: 1
   :widths: 18 43 26 40 33

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-10.1
     - Develop and apply policies in ZT solution tools to provide authorized user access to develop environment, source code management systems (e.g., artifact
       repositories).
     - ZT Security System
     - Only authorized users can access and perform actions on source code management systems.
     - PO.5.2
   * - B-10.2
     - Develop and apply ZT policies to endpoints, ensuring that code access is governed by organizational ZT policies.
     - ZT Security System
     - Only authorized endpoints can access source control systems and development systems.
     - PO.5.1
   * - B-10.3
     - Develop and apply ZT policies to only allow authorized users to modify restricted branches.
     - ZT Security System
     - Only authorized users can make changes to restricted branches.
     - PO.5.1
   * - B-10.4
     - Develop and apply policies in ZT solution tools to provide secure access for system-to-system communication.
     - Certificate Management System; ZT Security System
     - Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices,
       including rotation and short expiration times.
     - PO.5.1
   * - B-10.5
     - Develop and apply ZT policies to enforce compliance at each stage of the software delivery pipeline, permitting progression when explicit policy
       conditions are met.
     - ZT Security System
     - Only pipeline runs satisfying the applicable ZT policy conditions are permitted to advance.
     - PO.5.1

.. _scenario-b-11:

Scenario B-11: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components offer code generation and suggestion/completion capabilities. These capabilities interact with reactive activities; such as risk,
threat, or vulnerability management; or configuration management. Downstream components, such as SCMs or artifact repositories, can receive generated changes or
updated artifacts.

.. list-table::
   :header-rows: 1
   :widths: 18 45 27 42 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - B-11.1
     - Generates source code and configurations using user-provided context or requirements captured in ticketing systems.
     - AI Components; Configuration Management System; Developer Tools (e.g., IDE, CLI, and Binaries); IaC Scripts; SCM System; Ticketing System
     - Source code and configuration files are generated and changes, explanations, and commits are captured.
     - PW.5.1
   * - B-11.2
     - Generates remediations and feedback for detected flaws and defects in source code or configurations.
     - AI Components; Configuration Management System; Developer Tools (e.g., IDE, CLI, and Binaries); IaC Scripts; SCM System
     - Source code and configuration files are updated with generated changes and documented explanations.
     - PW.7.2
   * - B-11.3
     - Aligns code and configurations with known standards or required frameworks.
     - AI Components; Configuration Management System; Developer Tools (e.g., IDE, CLI, and Binaries); IaC Scripts; SCA System; SCM System
     - Code and configurations are brought into compliance with specified standards.
     - PW.5.1
   * - B-11.4
     - Refactors code to remediate risks, threats, or vulnerabilities identified during analysis.
     - AI Components; Configuration Management System; Developer Tools (e.g., IDE, CLI, and Binaries); IaC Scanner; IaC Scripts; SAST System; SCA System; SCM
       System; Secret Scanner
     - Vulnerabilities are remediated through refactored code and committed to SCM.
     - PW.7.2
   * - B-11.5
     - Analyzes the inclusion of software libraries and external dependencies based on known vulnerabilities.
     - AI Components; Artifacts Repository; Developer Tools (e.g., IDE, CLI, and Binaries); IaC Scanner; IaC Scripts; SCA System; SCM System
     - Dependency lists are optimized to remove or replace vulnerable libraries and updates are reflected in SCM or artifact repositories.
     - PW.8.2
   * - B-11.6
     - Automates the version control activities by managing commits, branches, and pull requests.
     - AI Components; Developer Tools (e.g., IDE, CLI, and Binaries); SCM System
     - Source code and source control artifacts are updated with generated commits, branches, and pull requests.
     - PW.6.2
   * - B-11.7
     - Evaluates software licenses of libraries or other external dependencies and suggests compliant alternatives.
     - AI Components; Artifact Repository; Developer Tools (e.g., IDE, CLI, and Binaries); SCA System; SCM System
     - Compliance requirements are provided and includes steps to replace non-compliant dependencies with acceptable alternatives.
     - N/A
   * - B-11.8
     - Detects potentially exposed credentials, certificates, or secrets and suggests possible remediations.
     - AI Components; Configuration Management System; Developer Tools (e.g., IDE, CLI, and Binaries); Credential Management System; SAST System; SCA System;
       SCM System; Secret Management System; Secret Scanner
     - Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or
       credentials.
     - PW.7.2
   * - B-11.9
     - Analyzes artifact repository reports to prioritize and mitigate security vulnerabilities.
     - AI Components; Artifact Repository; Developer Tools (e.g., IDE, CLI, and Binaries); SCM System
     - Plans are generated and provide methods to mitigate or remediate vulnerabilities found in artifacts.
     - PW.7.2

.. _scenario-build:

Phase C - Build
~~~~~~~~~~~~~~~

Automated pipelines transform code and configurations into deployable artifacts using ephemeral environments and integrated analysis to ensure quality,
security, and policy concurrence while providing feedback to teams.

.. _scenario-c-1:

Scenario C-1: Automate the Build Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Build process components are configured to use other tools and scripts to automate functions during the Build phase. These different components
automatically compile source code, integrate security tools, and create deployable artifacts in a repeatable and secure manner. Components will log errors and
status for feedback purposes.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 36 32

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-1.1
     - The build environment is provisioned which includes pipeline definitions, configurations, build tools, IaC and source code.
     - Build Tools (e.g., CLI and Binaries); CI/CD Pipeline; Configuration Management System; IaC Scripts; SCM System
     - CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed.
     - PO.3.1
   * - C-1.2
     - Configurations, IaC, and source code are obtained from SCM and Configuration Management Systems are used (e.g., applied, compiled, deployed, run, or
       transformed).
     - CI/CD Pipeline; Configuration Management System; IaC Scripts; SCM System
     - Configurations, IaC, and source code are obtained by CI/CD Pipelines and are used as part of the build process.
     - PO.3.2
   * - C-1.3
     - Build process steps are completed by the build environment. Output (e.g., compliance scores, vulnerabilities, audit logs, or other findings) are logged
       by each component.
     - CI/CD Pipeline
     - CI/CD Pipelines run all build process components, and each component generates output for tracking status and logging detailed information. (Note: all
       components needed in the pipeline are integrated here).
     - PO.3.3
   * - C-1.4
     - Current state of the build process is tracked by the SCM and Configuration Management System, which includes any logs or metadata provided by the CI/CD
       Pipeline.
     - CI/CD Pipeline; Configuration Management System; SCM System; Ticketing System
     - Errors that were captured by the CI/CD Pipelines are returned to SCM and Configuration Management Systems to track status and detailed information about
       the build process.
     - PO.3.2
   * - C-1.5
     - Approved configurations are applied to components (e.g., software, systems, and services) that are part of the build process.
     - Configuration Management System
     - Components and artifacts either deployed, managed, or used by the build process are leveraging approved configurations.
     - N/A
   * - C-1.6
     - New configurations created by the build process are added to the Configuration Management System.
     - CI/CD Pipeline; Configuration Management System
     - Components and artifacts that have been updated in the build are added to the configuration management system.
     - N/A

.. _scenario-c-2:

Scenario C-2: Implement Isolated/Hermetic environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Build environments should be isolated away from host systems or other environments to promote idempotency, separation of concerns, and immutable
outputs when possible. Install CLI tools and binaries to integrate security and code analysis components.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 38 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-2.1
     - Update the build environment with pipeline definitions, configurations, and IaC so that it is isolated from other environments.
     - CI/CD Pipeline; IaC Scripts; SCM System
     - The build environment is isolated from host systems or other environments and is automated.
     - PO.5.1
   * - C-2.2
     - Install CLI tools, binaries, and add software libraries required for the software application.
     - CI/CD Pipeline; Client tools; Software Libraries;
     - The CI/CD pipeline used CLI tools and binaries and accessed libraries within the isolated environment.
     - PO.5.2
   * - C-2.3
     - Create software artifacts to be stored in the artifact repository.
     - Artifact Repository; CI/CD Pipeline
     - Artifacts are created and stored in the artifact repository.
     - PO.5.2


.. _scenario-c-3:

Scenario C-3: Analyze Infrastructure as Code (IaC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Automate Infrastructure as Code to ensure consistent security baselines, enable rapid remediation of security vulnerabilities and compliance
issues, and maintain complete audit trails of all infrastructure changes.

.. list-table::
   :header-rows: 1
   :widths: 18 44 31 38 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-3.1
     - Automatically scan IaC artifacts for defects, vulnerabilities, insecure configuration, or compliance issues.
     - CI/CD Pipeline; Configuration Management System; IaC Scanner; SCA System; SCM System;
     - IaC Scanner identifies security vulnerabilities, insecure configurations, and compliance issues before IaC is executed.
     - N/A
   * - C-3.2
     - Log issues, resolve critical problems, and log infrastructure changes.
     - CI/CD Pipeline; Configuration Management system; IaC Scanner; Ticket System
     - Issues are created and may be resolved, and logs of configuration changes are maintained.
     - N/A
   * - C-3.3
     - Update the build environment based on the IaC scanner results.
     - CI/CD Pipeline; IaC Scanner; IaC Scripts; SCM System
     - Build environment is provisioned and managed based on scanned IaC artifacts to ensure consistency.
     - N/A

.. _scenario-c-4:

Scenario C-4: Integration of Software Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure that build pipelines automatically scan integrated software libraries for known vulnerabilities, license compliance issues, and security
risks.

.. list-table::
   :header-rows: 1
   :widths: 18 44 31 38 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-4.1
     - Automate the scanning of software libraries for known vulnerabilities, compliance issues, and security risks.
     - CI/CD Pipeline; Software Libraries; Artifact Repository; SCA System; SAST System
     - Vulnerabilities, compliance issues, and security risks from software libraries are identified.
     - PW.4.1
   * - C-4.2
     - Store software library artifacts in the artifact repository.
     - Artifact Repository; CI/CD Pipeline; Software Libraries
     - Software library artifacts used as part of the build are stored in the artifact repository.
     - PW.4.1


.. _scenario-c-5:

Scenario C-5: Perform Unit Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Individual components are tested to validate known functionality. Tools and processes are provided to perform validation tests for individual
components or functions of software systems or software applications. This can also provide reports describing discovered defects or code coverage issues.

.. list-table::
   :header-rows: 1
   :widths: 18 44 31 38 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-5.1
     - Execute the unit tests via the CI/CD pipeline.
     - CI/CD Pipeline; Unit Test Framework
     - Unit tests are pulled from SCM and run successfully against known functional criteria.
     - N/A
   * - C-5.2
     - Create and track unit test outputs and metadata from the results of the unit tests.
     - CI/CD Pipeline; SCM System; Ticketing System; Unit Test Framework
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results including issues (e.g., defects) in the ticketing system.
     - N/A

.. _scenario-c-6:

Scenario C-6: Automate Security Checks, Code Analysis, and Build Processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Build environments that perform automated security checks, code analysis, and build processes within the build environment as part of the
continuous integration pipeline.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-6.1
     - Configure CI/CD pipeline to automatically run security tools during the build to identify defects or vulnerabilities in source code and open
       source/closed source software libraries.
     - CI/CD Pipeline; IaC Scanner; Secrets Scanner; Lint Tool; SAST System; SCA System
     - CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed for security SAST, SCA, IaC Scanner, Secrets
       Scanner, and linting tools.
     - | PO.3.1
       | PO.3.2
       | PW.7.2
   * - C-6.2
     - Pull source code and scan for issues using security tools.
     - CI/CD Pipeline; Lint Tool; SAST System; SCA System; SCM System
     - Code is pulled from SCM, scanned, and each security tool generates results.
     - | PO.3.2
       | PW.7.2
   * - C-6.3
     - Provide notifications or logs to stakeholders based on findings.
     - CI/CD Pipeline; SAST System; SCA System
     - Security tools provide outputs of issues via notifications or logs to stakeholders.
     - | PO.3.3
       | PW.7.2

.. _scenario-c-7:

Scenario C-7: Securing Sensitive Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Build environments that use credentials, secrets, and variable management to store, track, and maintain sensitive information to prevent
unauthorized access and disclosure of sensitive information.

.. list-table::
   :header-rows: 1
   :widths: 18 44 33 37 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-7.1
     - Integrate the management systems and HSM into the CI/CD pipeline.
     - CI/CD Pipeline; Certificate Management System; Credential Management System; HSM; Secrets Management System
     - Sensitive information was securely retrieved during the build process.
     - PO.3.1
   * - C-7.2
     - Use credentials, secrets, and variable management systems to access and maintain credentials and secrets.
     - CI/CD Pipeline; Certificate Management System; Credential Management System; HSM; Secrets Management System
     - Sensitive information is protected by various management systems and HSMs to prevent unauthorized access and disclosure.
     - PO.3.1
   * - C-7.3
     - Automate the CI/CD pipeline to access credentials and secrets during the build.
     - CI/CD Pipeline; Certificate Management System; Credential Management System; Secrets Management System
     - The Build phase environment has authorized access to sensitive information with proper credentials and configuration.
     - PO.3.2
   * - C-7.4
     - Use HSM (including SW HSM) to protect digital assets.
     - Certificate Management System; CI/CD Pipeline; HSM
     - The HSM is tamper-resistant in maintaining digital assets (e.g., private keys and certificates).
     - PO.3.2

.. _scenario-c-8:

Scenario C-8: Detect Exposed Credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Secret scanners detect exposed sensitive information (e.g., credentials and API keys).

.. list-table::
   :header-rows: 1
   :widths: 18 45 28 37 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-8.1
     - Automate the CI/CD pipeline to run secret scanning tools.
     - CI/CD Pipeline; Secret Scanner
     - Source code or configuration credentials that are exposed are detected prior to the build.
     - PO.3.1
   * - C-8.2
     - Use SCA to track and analyze findings.
     - CI/CD Pipeline; SCA System; Secret Scanner
     - Findings are logged by SCA and stakeholders are notified.
     - PW.7.2

.. _scenario-c-9:

Scenario C-9: Securing Build Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure software packages and dependencies are securely stored and managed during the Build phase.

.. list-table::
   :header-rows: 1
   :widths: 18 45 30 36 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-9.1
     - Store all build artifacts in the artifact repository.
     - Artifact Repository; CI/CD Pipeline
     - Software packages (e.g., artifacts and dependencies) are securely stored and managed in the artifact repository.
     - N/A
   * - C-9.2
     - Log issues and updates of repositories for auditing purposes.
     - Artifact Repository; CI/CD Pipeline; Lint Tool; SAST System; SCA System
     - Information is logged by each tool for auditing of the build status.
     - N/A


.. _scenario-c-10:

Scenario C-10: Firmware Artifact Signing and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Use firmware management tools to maintain the firmware used within the environment.

.. list-table::
   :header-rows: 1
   :widths: 18 45 26 42 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-10.1
     - Use firmware management tools to sign and verify firmware signatures.
     - CI/CD Pipeline; Firmware Services
     - Signed firmware artifacts are verified and authentic.
     - N/A
   * - C-10.2
     - Log status and findings of firmware changes.
     - Firmware Services
     - Logs of firmware updates or changes are captured.
     - N/A


.. _scenario-c-11:

Scenario C-11: Artifact Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** The CI/CD pipeline verifies the integrity and authenticity of software components (e.g., source code, commits, container images, binaries, and
software libraries) using software certificates, checksums, or other cryptographic hashing functions before deployment to the test environment. Refer to
:ref:`Scenario B-7 Artifact Signing and Verification <scenario-b-7>` for details.


.. _scenario-c-12:

Scenario C-12: Creating Provenance of Generated Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure build environment scan the provenance of generated artifacts to verify and accept software, build processes, or data origins.

.. list-table::
   :header-rows: 1
   :widths: 19 46 26 43 26

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-12.1
     - Create, scan, and verify provenance of generated artifacts (e.g., SLSA attestation).
     - Attestation Signing and Verification Tool (e.g., SLSA); CI/CD Pipeline
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - PW.4.1
   * - C-12.2
     - Produce log for tracking purposes.
     - CI/CD Pipeline
     - Logs of results are available for tracking the provenance of generated artifacts.
     - N/A


.. _scenario-c-13:

Scenario C-13: Generate and Digitally Sign Software Bill of Materials (SBOM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** CI/CD pipeline Build environments automatically create a comprehensive SBOM, digitally sign the SBOM using trusted PKI to ensure its authenticity
and integrity across the software supply chain.

.. list-table::
   :header-rows: 1
   :widths: 19 46 27 41 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-13.1
     - Create a comprehensive SBOM.
     - CI/CD Pipeline; Provenance Generation and Verification Tool (e.g., Software Bill of Materials (SBOM))
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - PS.3.2
   * - C-13.2
     - Digitally sign the SBOM to ensure authenticity and integrity.
     - Artifact Signing and Verification Tool; Attestation Signing and Verification Tool; CI/CD Pipeline; Provenance Generation and Verification Tool (e.g.,
       SBOM)
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - PS.3.2
   * - C-13.3
     - Log output information related to the process of generating an SBOM for tracking.
     - CI/CD Pipeline
     - Outputs are logged by the CI/CD pipeline.
     - N/A


.. _scenario-c-14:

Scenario C-14: Analyze Container Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Container images are analyzed for vulnerabilities.

.. list-table::
   :header-rows: 1
   :widths: 18 45 27 41 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-14.1
     - Scan container images for security vulnerabilities prior to deploying them to the test environment.
     - CI/CD Pipeline; Container Image Scanner
     - Issues in container image software and configurations are identified.
     - N/A
   * - C-14.2
     - Run security tools to identify vulnerabilities.
     - CI/CD Pipeline; Lint Tool; SAST System; SCA System
     - Source code and libraries are analyzed for defects, vulnerabilities, licensing issues, and code standard violations; outputs are logged.
     - N/A
   * - C-14.3
     - Log outputs of the security tool scans.
     - CI/CD Pipeline; Lint Tool; SAST System; SCA System;
     - Logs of container scanner results, including issues, are produced.
     - N/A

.. _scenario-c-15:

Scenario C-15: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the ZT policies created in the Plan phase are implemented in this phase to ensure least privilege, secure access to the Build environment.

.. list-table::
   :header-rows: 1
   :widths: 19 47 28 33 33

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-15.1
     - Update and apply policies in ZT solution tools to provide authorized user access to build systems and applications based on user needs.
     - ZT Security System
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - PO.5.2
   * - C-15.2
     - Update and apply policies in ZT solution tools to provide authorized users access to source code management systems and artifact repositories based on
       user needs.
     - ZT Security System
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - PO.5.1
   * - C-15.3
     - Update ZT solutions to apply policies to the Build Phase infrastructure (e.g., VMs, host, OS’s, etc.) so that the CI/CD pipelines will run only if
       infrastructure meets policy requirements.
     - ZT Security System
     - Infrastructure attributes (VMs, hosts, OS, etc.) meet the policy requirements and CI/CD pipelines are allowed to execute.
     - PO.5.1
   * - C-15.4
     - Update and apply policies in ZT solution tools to protect secrets and credentials shared between the build environment and secrets/credential management
       tools.
     - ZT Security System
     - Secure communication is created between secrets/credential management tools and the build environment.
     - PO.5.1
   * - C-15.5
     - Protect classified Code Branches by assigning classification levels and applying ZT policies to restrict access to authorized users.
     - ZT Security System
     - Users with the required clearance can make changes to classified branches while those with lower clearance are denied access. Push and pull requests are
       logged for audit purposes.
     - PO.5.1
   * - C-15.6
     - Tag code branches with classification levels and apply ZT policies to prevent merging of branches that are in different classification levels.
     - ZT Security System
     - Merge requests should only succeed when the classification level requirements are met. Merge requests are logged for audit purposes.
     - PO.5.1
   * - C-15.7
     - Update and apply policies in ZT solution tools to provide authorized system service accounts access to build systems and applications.
     - ZT Security System
     - System service accounts’ access to build systems and applications are allowed or denied based on ZT policies.
     - PO.5.1
   * - C-15.8
     - Update and apply policies in ZT solution tools to protect build processes from utilizing container images from image registries that aren’t explicitly
       allowed.
     - ZT Security System
     - Build processes should only succeed when the container images are pulled from approved image registries specified in the ZT policies.
     - PW.4.1
   * - C-15.9
     - Update and apply policies in ZT solution tools to prevent sensitive secrets from being included in build artifacts.
     - ZT Security System
     - Build artifacts are scanned for sensitive secrets before being allowed to leave the build process. Unapproved artifacts containing secrets not
       whitelisted by the ZT policies are prevented from leaving the build environment.
     - PW.6.2
   * - C-15.10
     - Update and apply policies in ZT solution tools to provide secure system-to-system communication.
     - Certificate Management System; ZT Security System
     - Trusted communication is enforced across build systems using certificate-based authentication. Token-based authentication usage is limited and adheres to
       best practices, including rotation and short expiration times.
     - PO.5.1

.. _scenario-c-16:

Scenario C-16: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components provide automation for generating feedback in the form of suggestions or remediations. This feedback can cover many build-time
activities, such as flaw detections, compliance failures, or discovered vulnerabilities. Feedback can be recorded by Build phase components and used as input
into future iterations of the Continuous DevSecOps Lifecycle.

.. list-table::
   :header-rows: 1
   :widths: 19 47 28 33 33

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - C-16.1
     - Generates remediations and feedback for detected flaws and defects in source code or configurations.
     - AI Components; CI/CD Pipeline; Configuration Management System; IaC Scanner; SAST System; SCM System; Unit Test Framework
     - Source code and configuration files are updated with generated changes and documented explanations.
     - | PW.7.2
       | PW.9.1
   * - C-16.2
     - Identifies compliance gaps for required baselines, standards, or frameworks.
     - AI Components; CI/CD Pipeline; Configuration Management System; IaC Scanner; Lint Tool; SAST System; SCM System
     - Gaps and remediations for required standards are identified and provided as feedback.
     - PW.1.3
   * - C-16.3
     - Analyzes the inclusion of software libraries and external dependencies based on known vulnerabilities.
     - AI Components; Artifact Repository; CI/CD Pipeline; Container Image Scanner; SAST System; SCA System; SCM System
     - Changes and explanations for external dependency risks are generated and documented.
     - PW.4.1
   * - C-16.4
     - Detects potentially exposed credentials, certificates, or secrets and suggests possible remediations.
     - AI Components; CI/CD Pipeline; Certificate Management System; Credential Management System; HSM; SAST System; Secrets Management System; Secret Scanner
     - Exposed secrets are identified and feedback is provided to remediate improper storage or disclosure.
     - PW.7.2

.. _scenario-test:

Phase D - Test
~~~~~~~~~~~~~~

Teams use automated testing and ephemeral environments to evaluate deployable artifacts for functional and security requirements with CI/CD feedback guiding
future improvement.

.. _scenario-d-1:

Scenario D-1: Automate Test Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Provision the testing environment, automate different testing components, and collect testing results.

.. list-table::
   :header-rows: 1
   :widths: 19 47 28 33 33

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-1.1
     - The test environment is provisioned which includes pipeline definitions, configurations, IaC and executable code (e.g., source code and container
       images).
     - Artifact Repository; CI/CD Pipeline; Configuration Management System; Container Image Scanner; IaC Scripts; SCM System
     - The test environment is provisioned, so that the updated software can be tested.
     - PO.3.1
   * - D-1.2
     - Test process steps are completed by the CI/CD pipeline in the test environment. Output (e.g., compliance scores, vulnerabilities, audit logs, or other
       findings) are logged by each component.
     - CI/CD Pipeline; SAST System; SCA System
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - | PO.3.2
       | PO.3.3
   * - D-1.3
     - Current state of the test process is tracked by the Configuration Management System, which includes any logs or metadata provided by the CI/CD Pipeline.
     - CI/CD Pipeline; Configuration Management System
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track configuration status and detailed information
       about the test process.
     - PO.3.2
   * - D-1.4
     - The test environment is decommissioned after testing.
     - CI/CD Pipeline; Configuration Management System; IaC Scripts; SCM System
     - The resources used for the test environment have been freed up – no VMs, Containers, tools, or other environment components are still provisioned.
     - PO.3.2

.. _scenario-d-2:

Scenario D-2: Analyze IaC
^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Scan Infrastructure as Code scripts to ensure consistent security baselines, enable rapid remediation of security vulnerabilities and compliance
issues, and maintain complete audit trails of all infrastructure changes in the Test phase environment. Refer to :ref:`Scenario C-3: Analyze Infrastructure as Code
(IaC) <scenario-c-3>` for details.

.. _scenario-d-3:

Scenario D-3: Analyze Source Code for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Output from static analyzers is reviewed to identify security vulnerabilities.

.. list-table::
   :header-rows: 1
   :widths: 18 45 26 44 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-3.1
     - Configure CI/CD pipeline to automatically scan third-party artifacts for defects, vulnerabilities, or compliance issues.
     - CI/CD Pipeline; SCA System
     - SCA identifies security vulnerabilities and compliance issues before third-party artifacts are used.
     - | PO.3.1
       | PO.3.2
       | PW.4.1
   * - D-3.2
     - Configure CI/CD pipeline to automatically scan internal artifacts for defects, vulnerabilities, or compliance issues.
     - CI/CD Pipeline; SAST System; SCM System;
     - SAST identifies security vulnerabilities and compliance issues before internal artifacts can be used.
     - | PO.3.1
       | PO.3.2
       | PW.7.2
   * - D-3.3
     - Log issues and infrastructure changes.
     - CI/CD Pipeline; SAST System; SCA System; SCM System; Ticketing System
     - Issues are created in the ticketing system and logs of changes are maintained.
     - | PO.3.3
       | PW.7.2

.. _scenario-d-4:

Scenario D-4: Perform Unit Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Perform unit testing of all components and functions of the sample application to ensure it is working properly in the Test phase. Refer to
:ref:`Scenario C-5: Perform Unit Testing <scenario-c-5>` for details.

.. _scenario-d-5:

Scenario D-5: Perform Regression Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Application and system functionality (e.g., services, systems, and features) are tested to verify that defects haven’t been introduced as part of
changes to software and systems.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-5.1
     - Execute the regression tests via the CI/CD pipeline.
     - CI/CD Pipeline; Regression Test Tool; SCM System
     - Regression test scripts are pulled from SCM and run successfully against known regression criteria.
     - N/A
   * - D-5.2
     - Create and track regression test outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; Regression Test Tool; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - N/A

.. _scenario-d-6:

Scenario D-6: Perform Integration Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Software and systems components are tested to verify that new and existing software and system integrations function as expected.

.. list-table::
   :header-rows: 1
   :widths: 18 44 31 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-6.1
     - Execute the Integration tests via the CI/CD pipeline.
     - CI/CD Pipeline; Integration Test Tool; SCM System
     - Integration test scripts are pulled from SCM and run successfully against known integration criteria.
     - N/A
   * - D-6.2
     - Create and track integration test outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; Integration Tests; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - N/A


.. _scenario-d-7:

Scenario D-7: Perform Acceptance Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Usage and design patterns of software and systems are tested to verify that functionality still meets known requirements.

.. list-table::
   :header-rows: 1
   :widths: 18 44 31 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-7.1
     - Execute the acceptance tests via the CI/CD pipeline.
     - Acceptance Test Tool; CI/CD Pipeline; SCM System
     - Acceptance test scripts are pulled from SCM and run successfully against known acceptance criteria.
     - N/A
   * - D-7.2
     - Create and track acceptance test outputs and metadata from the results of the individual tests.
     - Acceptance Test Tool; CI/CD Pipeline; SCM System; Ticketing system
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - N/A


.. _scenario-d-8:

Scenario D-8: Perform Smoke Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Software and system components are tested to verify that running environments remain stable under expected usage patterns.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 39 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-8.1
     - Execute the smoke tests via the CI/CD pipeline.
     - CI/CD Pipeline; SCM System; Smoke Test Tool
     - Smoke test scripts are pulled from SCM and run successfully against known smoke test criteria.
     - N/A
   * - D-8.2
     - Create and track smoke test outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; Configuration Management System; SCM System; Smoke Test Tool; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - N/A

.. _scenario-d-9:

Scenario D-9: Dynamic Application Security Testing (DAST)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Leverage dynamic and analytical tools to identify and remediate security vulnerabilities.

.. list-table::
   :header-rows: 1
   :widths: 17 43 31 39 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-9.1
     - Execute the DAST tests via the CI/CD pipeline.
     - CI/CD Pipeline; DAST System
     - DAST tests are run successfully against security criteria.
     - | PO.3.2
       | PW.8.2
   * - D-9.2
     - Create and track DAST outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; DAST System; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - | PO.3.3
       | PW.8.2
   * - D-9.3
     - Inspect DAST outputs and metadata to provide vulnerability details.
     - CI/CD Pipeline; DAST System; ZT Security System
     - Output of report is inspected for vulnerability severity (e.g., CVE/CVSS score).
     - PW.8.2

.. _scenario-d-10:

Scenario D-10: Interactive Application Security Testing (IAST)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Use an IAST tool in the CI/CD pipeline to input security sensors directly into a running application during testing, providing real-time,
accurate feedback on vulnerabilities by analyzing code behavior, data flow, and HTTP traffic.

.. list-table::
   :header-rows: 1
   :widths: 17 43 31 39 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-10.1
     - Execute Acceptance or Functional testing.
     - Acceptance Test Tool; CI/CD Pipeline; SCM System
     - Acceptance or Integration test scripts are pulled from SCM and run successfully.
     - N/A
   * - D-10.2
     - While the tests are executing, execute IAST via the CI/CD pipeline.
     - CI/CD Pipeline; IAST System
     - IAST is run successfully against known security criteria.
     - N/A
   * - D-10.3
     - Create and track IAST outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; IAST System; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - N/A

.. _scenario-d-11:

Scenario D-11: Perform Fuzz Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Software and system components are tested to discover incorrect or unexpected behavior based on user input and software or system interactions.

.. list-table::
   :header-rows: 1
   :widths: 17 43 31 39 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-11.1
     - Execute the fuzz testing from the CI/CD pipeline.
     - CI/CD Pipeline; Fuzz Test Tool
     - Fuzz testing is run successfully.
     - | PO.3.2
       | PW.8.2
   * - D-11.2
     - Create and track Fuzz testing outputs and metadata from the results of the individual tests.
     - CI/CD Pipeline; Fuzz Test Tool; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - | PO.3.3
       | PW.8.2

.. _scenario-d-12:

Scenario D-12: Perform API Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Simulated usage and attacks are executed against API endpoints to discover or identify vulnerabilities such as broken authentication, injection
flaws, and improper data handling.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 39 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-12.1
     - Execute the API testing scripts from the CI/CD pipeline.
     - API Test Tool; CI/CD Pipeline; SCM System
     - API testing is run successfully.
     - | PO.3.2
       | PW.8.2
   * - D-12.2
     - Create and track API testing outputs and metadata from the results of the individual tests.
     - API Test Tool; CI/CD Pipeline; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - | PO.3.3
       | PW.8.2

.. _scenario-d-13:

Scenario D-13: CI/CD Execution, Test, and Security Policy Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Verify that the security policy for conducting the CI/CD pipeline and software testing is followed.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 39 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-13.1
     - Verify the CI/CD pipeline, automated test, and security policy.
     - CI/CD Execution, Test, and Security Policy Verification Tool; CI/CD Pipeline
     - The pipeline stops when the code violates the policy.
     - PO.3.2
   * - D-13.2
     - Log pipeline outputs and metadata from the results.
     - CI/CD Pipeline; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - PO.3.3

.. _scenario-d-14:

Scenario D-14: Firmware Artifact Integrity Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Explicitly verify the digital signatures and integrity of firmware binaries and components to ensure they have not been tampered with and are
from trusted sources before deployment. Refer to :ref:`Scenario C-10: Firmware Artifact Signing and Verification <scenario-c-10>` for details.

.. _scenario-d-15:

Scenario D-15: Artifact Scanning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** CI/CD pipeline verifies the integrity and authenticity of software components. Refer to
:ref:`Scenario B-7 Artifact Signing and Verification <scenario-b-7>` for details.

.. _scenario-d-16:

Scenario D-16: Assessing Data Provenance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** The CI/CD pipeline scans the provenance data of test artifacts to verify the origins of software or data. Refer to :ref:`Scenario C-12: Assessing
Provenance of Artifacts <scenario-c-12>` for details.

.. _scenario-d-17:

Scenario D-17: Verify Digitally Signed SBOM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Verify digitally signed SBOM. Refer to :ref:`Scenario C-13: Generate and Digitally Sign Software Bill of Materials (SBOM) <scenario-c-13>` for details.

.. _scenario-d-18:

Scenario D-18: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the ZT policies created in the Plan phase are implemented in this phase to ensure least privilege and secure access to the Test
environment.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-18.1
     - Update policies in ZT solution tools to provide authorized user access to test systems and applications based on user needs.
     - ZT Security System
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - PO.5.2
   * - D-18.2
     - Update policies in ZT solution tools to provide authorized users access to source code management systems and artifact repositories based on test user
       and developer needs.
     - ZT Security System
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - PO.5.1
   * - D-18.3
     - Update ZT solutions to apply policies to the Test Phase infrastructure (e.g., VMs, host, OS’s, etc.) so that the CI/CD pipelines will run only if
       infrastructure meets policy requirements.
     - ZT Security System
     - Infrastructure attributes (VMs, hosts, OS, etc.) meet the policy requirements and CI/CD pipelines are allowed to execute.
     - PO.5.1
   * - D-18.4
     - Update policies in ZT solution tools to protect secrets and credentials shared between the test environment and secrets/credential management tools.
     - ZT Security System
     - Secure communication is created between secrets/credential management tools and the test environment.
     - PO.5.1
   * - D-18.5
     - Apply policies to prevent software missing or failing mandatory tests from progressing to the next phase.
     - ZT Security System
     - Failing mandatory tests specified in ZT policies are blocked from advancing.
     - PO.5.1
   * - D-18.6
     - Update policies in ZT solution tools to provide secure system-to-system communication.
     - Certificate Management System; ZT Security System
     - Test Phase communications are secured using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices,
       including rotation and short expiration times.
     - PO.5.1
   * - D-18.7
     - Apply ZT policies to detect specific keywords in job logs
     - ZT Security System
     - If keywords are detected in job logs an incident report is created.
     - PO.5.1
   * - D-18.8
     - Apply ZT policies to block or exempt vulnerabilities found in security reports
     - ZT Security System; CI/CD Pipeline
     - CI/CD pipeline progression is blocked based on vulnerabilities found in security reports.
     - PO.5.1

.. _scenario-d-19:

Scenario D-19: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components can examine testing failures and provide feedback in the form of code changes or explanations to stakeholders. Output generated
from tests coupled with generated feedback can be preserved in different management components for use in other phases of the Continuous DevSecOps Lifecycle.

.. list-table::
   :header-rows: 1
   :widths: 17 42 39 31 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - D-19.1
     - Generates suggestions and remediations as feedback for detected flaws and defects in source code or configurations.
     - AI Components; CI/CD Pipeline; Configuration Management System; IaC Scanner; SAST System; SCM System; Unit Test Framework
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - | PW.7.2
       | PW.9.1
   * - D-19.2
     - Identifies gaps and remediations as feedback for required baselines, standards, or frameworks.
     - AI Components; CI/CD Pipeline; Configuration Management System; Lint Tool; IaC Scanner; SAST System; SCM System;
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - PW.1.3
   * - D-19.3
     - Generate changes, explanations, or suggestions based on analysis of software libraries or other external dependencies.
     - AI Components; Artifact Repository; CI/CD Pipeline; Container Image Scanner; SAST System; SCA System; SCM System
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - PW.4.1
   * - D-19.4
     - Identifies failing unit, integration, regression, acceptance, smoke, fuzz, or API testing as feedback.
     - Acceptance Test Tool; AI Components; API Test Tool; CI/CD Pipeline; Fuzz Test Tool; Integration Test Tool; Regression Test Tool; SCM System; Smoke Test
       Tool; Unit Test Framework
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - N/A
   * - D-19.5
     - Analyzes performance testing results and recommends optimizations.
     - AI Components; CI/CD Pipeline; SCM System
     - Performance bottlenecks are identified, and optimizations are provided.
     - N/A
   * - D-19.6
     - Evaluates security scan findings and proposes mitigation actions.
     - AI Components; CI/CD Pipelines; Container Image Scanner; SAST System; SCA System; SCM System
     - Security findings are summarized with actionable mitigation steps.
     - | PW.7.2
       | PW.8.2

.. _scenario-release:

Phase E – Release
~~~~~~~~~~~~~~~~~~

Automated processes package for distribution while teams coordinate releases, verify readiness and security, document changes, and collect feedback to improve
future releases.

.. _scenario-e-1:

Scenario E-1: Automation of Release and Delivery Processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Provision the Release environment and automate the release and delivery of artifacts.

.. list-table::
   :header-rows: 1
   :widths: 18 45 30 39 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-1.1
     - Provision the release environment which includes pipeline definitions, configurations, tools, IaC and executable code (e.g., container images).
     - Artifact Repository; CI/CD Pipeline; Configuration Management System; Container Image Scanner; IaC Scripts
     - The release environment is provisioned, so that the updated software can be released.
     - PO.3.1
   * - E-1.2
     - Release process steps are completed by the CI/CD pipeline in the release environment. Output (e.g., compliance scores, vulnerabilities, audit logs, or
       other findings) are logged by each component.
     - Acceptance Test Tool; CI/CD Pipeline; SAST System; SCA System; Smoke Test Tool
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - | PO.3.2
       | PO.3.3
   * - E-1.3
     - Current state of the release process is tracked by the Configuration Management System, which includes any logs or metadata provided by the CI/CD
       Pipeline.
     - CI/CD Pipeline; Configuration Management System
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track configuration status and detailed information
       about the Release process.
     - PO.3.2


.. _scenario-e-2:

Scenario E-2: Securing Release Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** The release artifacts and their dependencies are securely stored and managed.

.. list-table::
   :header-rows: 1
   :widths: 17 43 34 36 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-2.1
     - The pipeline stores artifacts in the release environment artifact repository.
     - Artifact Repository; CI/CD Pipeline
     - Artifacts created in this phase are securely stored in the Release phase artifact repository.
     - N/A
   * - E-2.2
     - Publish release artifacts and logs.
     - Artifact Repository; CI/CD Pipeline
     - Outputs are logged and artifacts can be released.
     - N/A


.. _scenario-e-3:

Scenario E-3: Manage Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Application and infrastructure configurations are managed and audited. Credentials, secrets, and certificate management are stored, tracked, and
maintained to prevent unauthorized access and disclosure of sensitive information in the Release environment.

.. list-table::
   :header-rows: 1
   :widths: 17 43 34 36 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-3.1
     - Maintain application and infrastructure configuration and enforce configuration compliance.
     - Certificate Management System; Configuration Management System; Credential Management System; Secrets Management System
     - Information (e.g., certificates, credentials and secrets, configuration versions) is maintained and secured by management systems.
     - N/A
   * - E-3.2
     - Create logs and findings for tracking and audit purposes.
     - Configuration Management System
     - Logs and incidents are recorded.
     - N/A

.. _scenario-e-4:

Scenario E-4: Manage Software Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure tools are properly managing software repositories and dependencies (e.g., software libraries or packages) for distribution, including
organizing, tracking, and securing distributed artifacts of released components.

.. list-table::
   :header-rows: 1
   :widths: 17 42 32 38 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-4.1
     - Create release packages using the package management system.
     - Package Management System
     - Release packages are completed for distribution.
     - N/A
   * - E-4.2
     - Organize, track, and secure artifacts for released components.
     - Package Management System
     - Artifacts are organized, tracked, and secured. Software dependencies; Licensing analysis results; Bugs or defects; Security vulnerabilities

       All software, including code, tools, and 3rd party libraries are running with the correct or expected versions.

     - PS.3.1


.. _scenario-e-5:

Scenario E-5: Coordinate Software Releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Release information (e.g., new features, bug fixes, and product enhancements) is collected to be included in planning and communicated to
stakeholders.

.. list-table::
   :header-rows: 1
   :widths: 17 42 34 36 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-5.1
     - Gather release information (e.g., new features, bug fixes, new configurations, product enhancements) to be included in the release process.
     - CI/CD Pipeline; Configuration Management System; Release Management System; Ticketing System
     - Release information is collected and documented.
     - N/A
   * - E-5.2
     - Provide audit logs and compliance information via the CI/CD pipeline.
     - CI/CD Pipeline
     - Audit logs and compliance information are documented and provided to stakeholders.
     - N/A

.. _scenario-e-6:

Scenario E-6: Document Release Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Collection of records and summaries that document the results of tests, scans, and compliance checks performed throughout the CI/CD pipeline,
providing proof that security and quality controls were executed and enabling traceability for audits and approvals before deployment.

.. list-table::
   :header-rows: 1
   :widths: 18 44 30 40 28

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-6.1
     - Gather test, scanning, and compliance logs.
     - CI/CD Pipeline; Configuration Management System; Release Management System; SCM System
     - The results from the testing phase are gathered and put with the release.
     - N/A

.. _scenario-e-7:

Scenario E-7: Perform Smoke Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Testers build tests to evaluate the stability of critical components and ensure that functionality in the release package is preserved and stable
as source code or build artifacts are changed. Refer to :ref:`Scenario D-8: Perform Smoke Testing <scenario-d-8>` for details.

.. _scenario-e-8:

Scenario E-8: Verify Release Criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Quality checks and automations are run to evaluate that software releases are cleared to proceed, that releases have been successful, and that
notifications are sent to stakeholders. Refer to :ref:`Scenario D-7: Perform Acceptance Testing <scenario-d-7>` for details.

.. _scenario-e-9:

Scenario E-9: Analyze Running Application for Vulnerabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Output from dynamic analyzers is reviewed to remediate security vulnerabilities.

.. list-table::
   :header-rows: 1
   :widths: 18 44 33 36 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-9.1
     - Execute the DAST tests via the CI/CD pipeline.
     - CI/CD Pipeline; DAST System
     - DAST tests are run successfully against security criteria.
     - | PO.3.2
       | PW.8.2
   * - E-9.2
     - Create and track DAST outputs and metadata from the results of the unit tests.
     - CI/CD Pipeline; Configuration Management System; DAST System; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - PW.8.2
   * - E-9.3
     - Execute Acceptance testing.
     - Acceptance Test Tool; CI/CD Pipeline; SCM System
     - Acceptance test scripts are pulled from SCM and run successfully against known integration criteria.
     - | PO.3.2
       | PW.8.2
   * - E-9.4
     - While the acceptance tests are executing, execute IAST via the CI/CD pipeline.
     - CI/CD Pipeline; IAST System
     - IAST is run successfully against known security criteria.
     - | PO.3.2
       | PW.8.2
   * - E-9.5
     - Create and track IAST outputs and metadata from the results of the unit tests.
     - CI/CD Pipeline; Configuration Management System; IAST System; SCM System; Ticketing System
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - PW.8.2

.. _scenario-e-10:

Scenario E-10: Firmware Release Readiness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Conduct final checks to ensure firmware binaries are securely packaged, correctly versioned, cryptographically verified for integrity and
authenticity, and meet all security and compliance requirements for release and deployment. Refer to :ref:`Scenario C-10: Firmware Artifact Signing and Verification
<scenario-c-10>` for details.

.. _scenario-e-11:

Scenario E-11: Artifact Signing and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Developers use artifact signing to establish and verify the integrity and authenticity of binaries and other components.

.. list-table::
   :header-rows: 1
   :widths: 17 42 32 38 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-11.1
     - Prior to software being deployed to the Operate environment, digitally sign the software components and artifacts.
     - Artifact Signing and Verification Tool; Certificate Management System; CI/CD Pipeline; HSM
     - Software components and artifacts (e.g., commits, images, binaries, or libraries; Signature files) are digitally signed and secrets are stored and
       protected by HSM.
     - PS.2.1
   * - E-11.2
     - Verify integrity and authenticity of software components and artifacts.
     - Artifact Signing and Verification Tool; CI/CD Pipeline
     - Results confirm that software components and artifacts are authentic and not tampered with.
     - PW.4.1
   * - E-11.3
     - Log status and findings of the results of integrity verification.
     - CI/CD Pipeline
     - Detailed logging is captured and alerts sent to stakeholders.
     - N/A

.. _scenario-e-12:

Scenario E-12: Analyze Container Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Container images for security vulnerabilities, misconfigurations, and embedded secrets are analyzed before deployment. Refer to :ref:`Scenario C-14:
Analyze Container <scenario-c-14>` for details.


.. _scenario-e-13:

Scenario E-13: Validate Software and Data Origins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** All software components, data, and their origins are verified and validated to ensure the integrity, traceability, and security of the software
supply chain before deployment. Refer to :ref:`Scenario C-12: Assessing Provenance of Artifacts <scenario-c-12>` and :ref:`Scenario C-13: Generate and Digitally Sign Software Bill of Materials (SBOM) <scenario-c-13>` for details.

.. _scenario-e-14:

Scenario E-14: Analyze IaC
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Automated analysis of Infrastructure as Code for security vulnerabilities and compliance issues. Refer to :ref:`Scenario C-3: Analyze Infrastructure as
Code (IaC) <scenario-c-3>` for details.

.. _scenario-e-15:

Scenario E-15: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the ZT policies created in the Plan phase are implemented in this phase to ensure least privilege and secure access to the Release
environment.

.. list-table::
   :header-rows: 1
   :widths: 17 43 29 41 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-15.1
     - Update policies in ZT solution tools to provide authorized user access to release management systems and applications based on user needs.
     - ZT Security System
     - Users’ access to release systems and applications are allowed or denied based on ZT policies.
     - PO.5.2
   * - E-15.2
     - Update ZT solutions to apply policies to the Release Phase infrastructure (e.g., VMs, host, OS’s, etc.) to allow for the execution of tools to release
       secured artifacts only if infrastructure meets policy requirements.
     - ZT Security System
     - Infrastructure meets the policy requirements and tools are allowed to execute.

       Only artifacts deemed safe by the DevSecOps tools and ZT policies are released.

     - PO.5.1
   * - E-15.3
     - Update policies in ZT solution tools to ensure release and deployment certificates, credentials, and secrets stored on the file system are secured.
     - ZT Security System
     - Certificates, credentials, and secrets stored on the file system are protected and shared securely. Communications between systems are secured by ZT
       policies.
     - PO.5.1
   * - E-15.4
     - Apply policies to ensure that only signed and validated software is released.
     - ZT Security System
     - Only software proven to originate from the approved build and test phase processes in compliance with ZT policies are staged for release.
     - PO.5.1

.. _scenario-e-16:

Scenario E-16: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components can generate notifications, vulnerability reports, and release notes that describe the scoping of changes and the overall status to
stakeholders. Feedback generated during the Release phase can be augmented with testing output, dependency scans, and compliance reports to provide input for
future planning and improvement.

.. list-table::
   :header-rows: 1
   :widths: 17 42 39 31 31

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - E-16.1
     - Propose remediations and feedback for detected flaws and defects during release.
     - Artifact Repository; CI/CD Pipeline; Configuration Management System; IaC Scripts; SAST System; SCA System; SCM System
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - | PW.7.2
       | PW.9.1
   * - E-16.2
     - Identifies failing acceptance and smoke testing as feedback.
     - Acceptance Test Tool; AI Components; CI/CD Pipeline; SCM System; Smoke Test Tool
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - N/A
   * - E-16.3
     - Analyzes the inclusion of software libraries and external dependencies based on known vulnerabilities.
     - AI Components; Artifact Repository; CI/CD Pipeline; Container Image Scanner; IAST System; Package Management System; SCA System; SCM System
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - PW.4.1
   * - E-16.4
     - Detects potentially exposed credentials, certificates, or secrets and suggests possible remediations.
     - AI Components; CI/CD Pipeline; Certificate Management System; Credential Management System; HSM; SAST System; Secrets Management System
     - Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or
       credentials.
     - PW.7.2
   * - E-16.5
     - Validates release artifacts against required baselines, standards, or frameworks.
     - AI Components; CI/CD Pipeline; Configuration Management System; IaC Scanner; Lint Tool; Release Management System; SAST System; SCM System; Ticketing
       System
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - PW.1.3
   * - E-16.6
     - Automates release notifications and event generation for scope and status.
     - CI/CD Pipeline; Configuration Management System; Release Management System; Ticketing System
     - Release status and scope notifications are generated and distributed to stakeholders.
     - N/A

.. _scenario-deploy:

Phase F - Deploy
~~~~~~~~~~~~~~~~

Automated pipelines install and configure software on production infrastructure while teams monitor deployments, verify security and performance, and collect
feedback to ensure reliable, secure, and consistent releases.


.. _scenario-f-1:

Scenario F-1: Automate the Deployment Processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Provision the Deployment environment and orchestrate software releases (e.g., application deployments, final tests/checks, notifications, and
manual approvals).

.. list-table::
   :header-rows: 1
   :widths: 18 44 35 35 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - F-1.1
     - The Deployment environment is updated/provisioned which includes pipeline definitions, configurations, tools, IaC and executable code (e.g., container
       images).
     - Artifact Repository; CI/CD Pipeline; Configuration Management System; IaC Scripts
     - The deployment environment is provisioned, so that the updated software can be deployed.
     - PO.3.1
   * - F-1.2
     - Deployment process steps are completed by the CI/CD pipeline in the Deployment environment. Outputs are logged by each component.
     - CI/CD Pipeline
     - CI/CD Pipelines run all deployment process components, and each component generates output for tracking status and logging detailed information.
     - | PO.3.2
       | PO.3.3
   * - F-1.3
     - Current state of the Deployment process is tracked by the Configuration Management System, which includes any logs or metadata provided by the CI/CD
       Pipeline.
     - CI/CD Pipelines; Configuration Management System
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track configuration status and detailed information
       about the Release process.
     - PO.3.2

.. _scenario-f-2:

Scenario F-2: Securing Deployment Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure deployable software packages and dependencies are securely stored and managed. See :ref:`Scenario E-2: Securing Release Artifacts <scenario-e-2>` for
demonstration steps.


.. _scenario-f-3:

Scenario F-3: Manage System and Application Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Application and infrastructure configurations are managed and audited. Certificates, credentials, and secrets are stored, tracked, and managed
(e.g., issuance, rotation, revocation) to prevent unauthorized access and disclosure of sensitive information in the Release environment. Refer to :ref:`Scenario E-3:
Manage Configurations <scenario-e-3>` for demonstration details.

.. _scenario-f-4:

Scenario F-4: Manage Software Releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Notifications about upcoming software release (e.g., release version, application details, software dependencies, test results, and configuration
changes) are collected and delivered to stakeholders. Refer to :ref:`Scenario E-5: Coordinate Software Releases <scenario-e-5>` for demonstration details.

.. _scenario-f-5:

Scenario F-5: Analyze IaC
^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Automate analysis of Infrastructure as Code for security vulnerabilities and compliance issues. Refer to :ref:`Scenario C-3: Analyze Infrastructure as Code
(IaC) <scenario-c-3>` for details.


.. _scenario-f-6:

Scenario F-6: Manage Software Supply Chain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** SBOM artifacts are managed, analyzed, and verified as part of the deployment process. Metadata, logs, and status are collected to maintain
transparency and to provide visibility into the provenance of an application and its dependencies.

.. list-table::
   :header-rows: 1
   :widths: 18 44 33 36 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - F-6.1
     - Analyze and verify SBOM and provenance data generated from deployable artifacts.
     - CI/CD Pipeline; Provenance Verification (e.g., SBOM)
     - SBOM and other provenance data are verified before deployment.
     - N/A
   * - F-6.2
     - The SBOM process is tracked by the Configuration Management System, which includes any logs or metadata provided by the CI/CD Pipeline.
     - CI/CD Pipeline; Configuration Management System
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the SBOM
       process.
     - N/A


.. _scenario-f-7:

Scenario F-7: Secure Firmware Deployment and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the secure installation of verified firmware onto target devices and manage its operational configurations in alignment with security
policies.

.. list-table::
   :header-rows: 1
   :widths: 17 43 34 36 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - F-7.1
     - Verify integrity and authenticity of firmware components and artifacts.
     - CI/CD Pipeline; Firmware Management System
     - Results confirm that firmware components and artifacts are authentic and not tampered with.
     - N/A
   * - F-7.2
     - Accept or reject software components and artifacts based on verification results.
     - CI/CD Pipeline
     - Software components and artifacts that are verified are accepted.
     - N/A
   * - F-7.3
     - Deploy firmware.
     - CI/CD Pipeline; Firmware Management System
     - Firmware is up to date on all hardware components.
     - N/A

.. _scenario-f-8:

Scenario F-8: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the ZT policies created in the Plan phase are implemented in this phase to ensure least privilege and secure access to the Deploy
environment.

.. list-table::
   :header-rows: 1
   :widths: 17 43 36 34 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - F-8.1
     - Update policies in ZT solution tools to provide access to users who manage the deployment process.
     - ZT Security System
     - Users’ access to the deploy phase environment are allowed or denied based on ZT policies.
     - PO.5.2
   * - F-8.2
     - Update monitoring systems and automated tools with ZT policies to ensure systems communicate to other systems on a needed basis only.
     - ZT Security System
     - System-to-system communications are restricted based on functionality and ZT policies.
     - PO.5.1
   * - F-8.3
     - Apply policies to ensure that only signed and validated software is deployed.
     - ZT Security System
     - Only software proven to originate from the approved build and test phase processes are deployed.
     - PO.5.1
   * - F-8.4
     - Apply policies to ensure that data residency requirements are enforced
     - ZT Security Platform
     - Only software that meets data residency requirements are deployed.
     - PO.5.1

.. _scenario-f-9:

Scenario F-9: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components can process and provide curated feedback to stakeholders during the Deploy phase of the Continuous DevSecOps Lifecycle. CI/CD
Pipelines generate input that feeds into AI components as context. These AI components can generate summarizations of identity risks that impact deployments and
released artifacts. AI can also provide compliance and standards analysis of deployed components while suggesting remediations to detect flaws or defects, which
can be leveraged as part of future improvements to software and systems.

.. list-table::
   :header-rows: 1
   :widths: 17 42 39 35 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - F-9.1
     - Generates suggestions and remediations as feedback for detected flaws and defects in deployments.
     - AI Components; Artifact Repository; CI/CD Pipeline; Configuration Management System; IaC Scripts; SCM System
     - Suggestions and remediation guidance are provided and documented for the identified deployment issues.
     - | PW.7.2
       | PW.9.1
   * - F-9.2
     - Provides mitigations for risks, threats, or vulnerabilities based on reporting from artifact repository.
     - AI Components; Artifact Repository; Artifact Signing and Verification Tool; CI/CD Pipeline; SCM System
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - PW.4.1
   * - F-9.3
     - Identifies disclosed credentials, secrets, certificates, or other sensitive information as feedback.
     - AI Components; Certificate Management System; CI/CD Pipeline
     - Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure.
     - PW.7.2
   * - F-9.4
     - Identifies gaps and remediations as feedback for required baselines, standards, or frameworks.
     - AI Components; CI/CD Pipeline; Configuration Management System; Deployment Management System; SCM System; Ticketing System
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - PW.1.3
   * - F-9.5
     - Provides configuration changes to address functional problems or security risks in deployment configurations.
     - AI Components; CI/CD Pipeline; IaC Scanner; Configuration Management System; SCM System
     - Configuration changes are generated in configuration management system.
     - PW.9.1
   * - F-9.6
     - Generates events and notifications for providing scope and status of deployment.
     - AI Components; CI/CD Pipeline; Configuration Management System; Deployment Management System; Ticketing System
     - Deployment status and scope notifications are generated and documented in project or deployment management systems.
     - N/A

.. _scenario-operate:

Phase G - Operate
~~~~~~~~~~~~~~~~~

Teams use automated monitoring and evidence collection to ensure the integrity, security, and reliability of production systems, using feedback to address
issues and guide continuous improvement.

.. _scenario-g-1:

Scenario G-1: Manage Application Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Operational environments are developed and maintained to provide secure, isolated, and scalable infrastructure to an application, its
dependencies, and configurations.

.. list-table::
   :header-rows: 1
   :widths: 17 42 36 38 27

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - G-1.1
     - The Operate environment is provisioned which includes pipeline definitions, configurations, tools, IaC and executable code.
     - CI/CD Pipeline; Configuration Management System; IaC Scripts; Runtime Signature Verification Tool
     - The Operate environment is provisioned, so that the software may run.
     - PO.3.1
   * - G-1.2
     - Operate process steps are completed by the CI/CD pipeline in the Operate environment. Outputs are logged by each component.
     - CI/CD Pipeline; IaC Scripts
     - CI/CD Pipelines run all deployment process components in the Operate environment, and each component generates output for tracking status and logging
       detailed information.
     - | PO.3.2
       | PO.3.3
   * - G-1.3
     - Current state of the Operate process is tracked by the Configuration Management System, which includes any logs or metadata provided by the CI/CD
       Pipeline.
     - CI/CD Pipeline; Configuration Management System
     - The current state that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about
       the Release process.
     - PO.3.2

.. _scenario-g-2:

Scenario G-2: Manage SBOMs for Deployed Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** SBOM artifacts are collected and published for stakeholders to use when verifying the integrity and authenticity of a software application and
its components. Refer to :ref:`Scenario F-6: Manage Software Supply Chain <scenario-f-6>` for details.

.. _scenario-g-3:

Scenario G-3: Validate Software Artifact Integrity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Digital signatures of runtime components are frequently validated to ensure the integrity and authenticity of a software application and its
components. Refer to :ref:`Scenario C-12: Assessing Provenance of Artifacts <scenario-c-12>` and :ref:`Scenario C-13: Generate and Digitally Sign Software Bill of Materials (SBOM) <scenario-c-13>` for details.

.. _scenario-g-4:

Scenario G-4: Firmware Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Provide systems to monitor new vulnerabilities discovered in firmware deployed in the field, alerting to the need for a firmware update. Provide
systems to monitor system health with telemetry and predictive analysis for failures. Provide systems to monitor sustainability. Use firmware management tools to maintain firmware that is used within the Operate environment. Refer to :ref:`Scenario B-6: Firmware Development <scenario-b-6>` for details.

.. _scenario-g-5:

Scenario G-5: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure the zero trust policies created in the Plan phase are implemented in this phase to ensure least privilege, secure access to the Operate
environment.

.. list-table::
   :header-rows: 1
   :widths: 18 44 32 38 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - G-5.1
     - Update policies in ZT solution tools to provide access to users who manage the operate environment.
     - ZT Security System
     - Users’ access to the operate phase environment are allowed or denied based on ZT policies.
     - PO.5.2
   * - G-5.2
     - Update monitoring systems logging, and security tools with ZT policies to ensure systems communicate to other systems on a needed basis only.
     - ZT Security System
     - System-to-system communications are restricted based on functionality and ZT policies.
     - PO.5.1
   * - G-5.3
     - Apply policies to detect unauthorized changes to application configuration.
     - ZT Security System
     - Unauthorized changes and vulnerabilities are detected and reported based on the ZT policies.
     - PO.5.1

.. _scenario-g-6:

Scenario G-6: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components can generate suggestions and remediations necessary to address operational issues. CI/CD Pipeline components can feed new findings
and context into AI-supported management tools to describe necessary changes and document new findings. These components can then generate security and
compliance recommendations that can be implemented as part of future iterations of the Continuous DevSecOps Lifecycle.

.. list-table::
   :header-rows: 1
   :widths: 18 43 40 35 24

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - G-6.1
     - Generates suggestions and remediations as feedback for detected flaws and defects in source code or configurations.
     - AI Components; Artifact Repository; CI/CD Pipeline; Configuration Management System; Container Image Scanner; IaC Scripts; SCM System
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - RV.1.3
   * - G-6.2
     - Identifies gaps and remediations as feedback for required baselines, standards, or frameworks.
     - AI Components; Artifact Repository; Artifact Signing and Verification Tool; CI/CD Pipeline; SCM System
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - PW.4.1

.. _scenario-continuous-improvements:

Phase H – Continuous Improvements, Security, and Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This consists of a collection of components and activities that appear throughout the DevSecOps lifecycle and enable the functional and security requirements of
a given phase.

.. _scenario-h-1:

Scenario H-1: Manage Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** All environments are developed and maintained to provide secure, isolated, and scalable infrastructure to applications, their dependencies, and
configurations. Refer to :ref:`Scenario A-5 <scenario-a-5>`, :ref:`Scenario A-6 <scenario-a-6>`, :ref:`Scenario A-7 <scenario-a-7>`, :ref:`Scenario F-1 <scenario-f-1>`, and :ref:`Scenario E-3 <scenario-e-3>` for demonstration details.

.. _scenario-h-2:

Scenario H-2: Examine Outcomes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Development, security, and operations team members document, coordinate, communicate, and resolve operational and security concerns, and maintain
system and application functionality.

.. list-table::
   :header-rows: 1
   :widths: 18 44 32 38 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - H-2.1
     - Examine past outcomes to guide improvements to team members via training.
     - Team Collaboration Tools; Ticketing System
     - Improvements to the team members working on the software project.
     - PO.2.2
   * - H-2.2
     - Examine past outcomes to guide improvements to DevSecOps process.
     - Risk Management System; Ticketing System
     - Improvements to the processes used during the development and testing of the software project.
     - PO.1.2
   * - H-2.3
     - Examine past outcomes to guide improvements to the CI/CD pipeline and related tooling.
     - CI/CD Pipeline; Certificate Management System, Configuration Management System, Credential Management System, Firmware Services, HSM, Risk Management
       System, SCM System, Secrets Management System, Team Collaboration Tools, Threat Modeling System, Ticketing System
     - Improvements to the tools used during the development and testing of the software project.
     - PO.3.2

.. _scenario-h-3:

Scenario H-3: Monitor Infrastructure and Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Systems monitor (e.g., probes, agents, logging, and continuous monitoring), collect, analyze, and detect infrastructure and application changes
to identify performance trends and system or application anomalies, throughout the DevSecOps Lifecycle.

.. list-table::
   :header-rows: 1
   :widths: 18 44 33 36 29

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - H-3.1
     - Application Monitoring tools log activity in the application and create tickets if problems are detected.
     - CI/CD Pipeline; Operations Monitoring System (e.g., Infrastructure Management, Log Management, and Performance Monitoring); Ticketing System
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - N/A
   * - H-3.2
     - Network Monitoring tools log activity in the network and create tickets if problems are detected.
     - CI/CD Pipeline; Operations Monitoring System; Ticketing System
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - N/A

.. _scenario-h-4:

Scenario H-4: Monitor Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Provide security monitoring capabilities such as vulnerability management, incident management, Security Information and Event Management (SIEM),
and Security Orchestration, Automation and Response (SOAR).

.. list-table::
   :header-rows: 1
   :widths: 17 43 33 37 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - H-4.1
     - Security Monitoring tools log activity in the application and create tickets if problems are detected.
     - CI/CD Pipeline; Security Monitoring Systems; Ticketing System
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - PO.5.2
   * - H-4.2
     - Vulnerability Monitoring tools continuously query external sources for publicly disclosed vulnerability information and create tickets if problems are
       confirmed.
     - CI/CD Pipeline; Security Monitoring Systems; Ticketing System
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - RV.1.1
   * - H-4.3
     - Establish a process to enable external sources to responsibly disclose previously undiscovered issues before making the issue public and create tickets
       if problems are confirmed.
     - Security Monitoring Systems; Ticketing System
     - The responsible disclosure of new vulnerabilities discovered by external sources.
     - RV.1.3

.. _scenario-h-5:

Scenario H-5: Manage Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Use firmware management tools to maintain firmware that is used within all environments. Refer to :ref:`Scenario B-6: Firmware Development <scenario-b-6>` for details.

.. _scenario-h-6:

Scenario H-6: Zero Trust Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** Ensure Zero Trust policies, including those enforcing least privilege access and device posture validation, are enforced throughout all phases of
the DevSecOps lifecycle. Common data security policies for sensitive data, artifacts, and environments are applied to user access, use, sharing, and
distribution. All principles and policies should be documented and have audit trails.

.. list-table::
   :header-rows: 1
   :widths: 17 43 31 39 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - H-6.1
     - Update policies in ZT solution tools to provide authorized user access to release management systems and applications based on user needs.
     - ZT Security System
     - Users’ access to release systems and applications are allowed or denied based on ZT policies.
     - PO.5.2
   * - H-6.2
     - Update monitoring systems and automated tools with ZT policies to ensure systems communicate to other systems on a needed basis only.
     - ZT Security System
     - System-to-system communications are restricted based on functionality and ZT policies. Communications are secured using certificate-based authentication.
     - PO.5.1
   * - H-6.3
     - Update ZT policies to restrict modifications to restricted branches to only the users that have the authorization to access them.
     - ZT Security System
     - Authorized users can make changes to restricted branches.
     - PO.5.1
   * - H-6.4
     - Update ZT solutions to integrate with software security tools (e.g., SAST, SCA, Lint tools).
     - ZT Security System
     - Validated secured code are permitted to be used in the build.
     - PO.5.1
   * - H-6.5
     - Update policies in ZT solution tools to ensure certificates, credentials, and secrets stored on the file system.
     - ZT Security System
     - Certificates, credentials, and secrets stored on the file system are protected and shared securely. Communications between systems are secured by ZT
       policies.
     - PO.5.1
   * - H-6.6
     - Apply policies to detect unauthorized changes to application configuration.
     - ZT Security System
     - Any unauthorized configuration changes are detected and reported. Configuration changes must be done through approved processes.
     - PS.1.1

.. _scenario-h-7:

Scenario H-7: AI Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Objective:** AI components can ingest feedback from the components throughout the Continuous DevSecOps Lifecycle. These components can generate reports that
describe risks and anomalies. Management tools can leverage these AI components to build context in the form of new tickets, issues, or work items.

.. list-table::
   :header-rows: 1
   :widths: 17 43 40 30 30

   * - **Scenario ID**
     - **Demonstration Step**
     - **Component(s)**
     - **Expected Outcome**
     - **SSDF Task**
   * - H-7.1
     - Identifies risks, generates reports, monitors exposure and triggers mitigations.
     - AI Components; CI/CD Pipeline; Configuration Management System; Cyber Intelligence, Threat, and Security Metadata Feeds; Risk Management System;
       Ticketing System
     - Risk reports are generated, and mitigation actions are triggered in risk management or ticketing systems.
     - PW.1.1
   * - H-7.2
     - Analyzes historic incidents, extracts improvement themes and creates actionable backlog items.
     - AI Components; CI/CD Pipeline; Certificate Management System; Configuration Management System; Credential Management System; Firmware Services; HSM; Risk
       Management System; SCM System; Secret Management System; Team Collaboration Tools; Threat Modeling System, Ticketing System
     - Improvement themes are identified, and new actionable items are created in the project backlog.
     - | RV.3.1
       | RV.3.2
       | RV.3.3
       | RV3.4
