Appendix B Component Description 
=================================

The following table details the components described in this document, including their descriptions. For the purposes of this document, System refers to a standalone tool or an integrated suite of tools designed to deliver specific functionality.

.. glossary::

   Acceptance Test Tool
      Provides the tools and scripts necessary to validate that expected changes meet requirements.

   API Test Tool
      Provides the tools and scripts to evaluate the requirements of application programming interfaces (APIs) by simulating various functional and attack
      scenarios to identify failures and vulnerabilities within the test environment.

   Artifact Repository (e.g., Internal and External)
      Manages the secure storage and retrieval of software artifacts (i.e., software libraries, docker images, virtual machine images, or other software
      system or software application dependencies) hosted from internal or externally available artifact repositories.

   Artifact Signing and Verification Tool
      Digitally signs and verifies software components and artifacts could consist of source code, commits, docker images, binaries, and software libraries
      using software certificates, checksums, or other hashing functions. This can also establish the authenticity and integrity of software components and
      artifacts to help detect unauthorized use or tampering.

   Attestation Signing and Verification Tool 
      Generates and verifies the digitally signed artifact (e.g., SLSA) that both provides provenance information such as artifacts produced, processes, and any included dependencies
      in addition to information captured during the generation of the artifact (i.e., CI/CD components used, source code changes, etc.). 

   Build Tools (e.g., CLI, and Binaries)
      Consists of command line interfaces (CLIs), software development kits (SDKs), and commercially available or open-source binaries, plugins, or
      extensions. These components enable the CI/CD pipeline to build software from code.

   Certificate Management System
      Manages the secure storage, issuance, renewal, and revocation of cryptographic material associated with software certificates. This can include
      lifecycle management, certificate templates or profiles, and policy controls.

   CI/CD Execution, Test and Security Policy Verification Tool
      Verifies that actions and results meet the CI/CD and test and security policies.

   CI/CD Pipeline
      Provides continuous functionality in develop/build/test/release/deploy/operate phases. It uses tools and scripts to build environments, source code,
      docker images, and other software artifacts. This also provides an integration point for test and security tools (i.e., SAST, SCA, lint tool, or other
      scanners). Each environment should be self-contained to prevent the leaking of software or configuration artifacts between other environments. Results
      from the pipeline are used in prior phases to inform planning and changes.

   Configuration Management System
      Manages the creation, assignment, and tracking of configuration items and artifacts. These items and artifacts are used to build and configure system or
      software baselines and to detect configuration drift.

   Container Image Scanner
      Scans images and containerized assets for security vulnerabilities (i.e., vulnerable software packages, base images, and configurations).

   Credential Management System
      Manages, protects, and maintains software system or software application credentials (i.e., usernames, passwords, API keys, or secrets) that are
      assigned to individuals or groups of individuals (e.g., internal users, customers, or external parties). This can also include configuration, policy
      settings, or audit controls that are used to govern and monitor access to credentials.

   Cyber Intelligence, Threat, and Security Metadata Feeds (e.g., OpenSSF, National Vulnerability Database (NVD), Open Source Vulnerabilities (OSV), and Common Vulnerabilities and Exposures (CVE)/ Common Weakness Enumeration (CWE))
      Provides tools and processes to review independently verified cyber intelligence, threat actors or campaigns, software vulnerabilities, and other
      security relevant information. This can include the identification of new security requirements, new threat models, or newly discovered risks to
      software systems, software applications, or personnel.

   DAST System
      Analyzes the running state of a software system or software application through simulation of known use cases or real-world attack vectors to identify
      defects or security vulnerabilities.

   Deployment Management System (e.g., Release Orchestration, Rollback, and Canary)
      Manages the deployment of artifacts into the operational environment. This can include different strategies (i.e., canary-based, rolling, blue/green,
      red/black, or testing in production) to control deployment of software/system assets, feature components, and configurations into the operational
      environment.

   Developer Tools (e.g., IDE, CLI, and Binaries)
      Consists of integrated developer environments (IDEs), command line interfaces (CLIs), software development kits (SDKs), and commercially available or
      open-source binaries, plugins, or extensions. These components enable software developers, operations, and security personnel to create, build, or
      modify, product features, security controls/policies, automation scripts, or services associated with software systems or software applications.

   Firmware Services
      Provides comprehensive capabilities for managing device firmware securely throughout its lifecycle. It supports initial development, vulnerability
      scanning, remediation, secure updates, ongoing monitoring and reporting.

   Fuzz Test Tool
      Provides the tools and scripts to discover defects or security vulnerabilities by generating invalid, unexpected, or random input to a running software
      or system component within the test environment.

   Hardware Security Module (HSM) (including Software or Virtual HSMs)
      Provides a tamper-resistant security and management component for maintaining digital assets (i.e., private keys and certificates) used for
      cryptographic processing.

   IaC Scanner
      Scans infrastructure as code artifacts for defects, vulnerabilities, or security issues prior to executing the IaC scripts.

   IaC Scripts
      Creates or modifies infrastructure resources (i.e., hosts, networks, and services) as part of the provisioning and management of various deployment
      environments and during the develop, build, test, release, deploy and operate phases.

   IAST System
      Analyzes system interactions with software systems or running software applications using sensors, canaries, or other mechanisms within the current
      environment. This can also provide latency information, code execution graphs, data flow, and logging functionality.

   Integration Test Tool
      Provides the tools and scripts to verify requirements are in place for integrations between different components of software systems or software
      applications within the testing environment.

   Lint Tool
      Analyzes source code for non-standard or code style issues, potential defects, or code standard violations prior to committing source code.

   Operations Monitoring System (e.g., Infrastructure Management, Log Management, and Performance Monitoring)
      Manages the collection, analysis, and assessment of infrastructure, software systems and software applications hosted in the operational environment. It
      also includes generation of logs, detected defects/vulnerabilities, and system statuses.

   Package Management System
      Collects release packages by utilizing software repositories and dependencies (i.e., software libraries or packages) for distribution. This can include
      tools and processes to organize, track, and secure distributed artifacts.

   Product Management System
      Manages and maintains the organizational requirements necessary to deliver products, features, and functionality to stakeholders. This can include
      documentation on product vision or roadmaps, growth strategy, as well as security-relevant concerns for stakeholders.

   Project Management System (e.g., Team Planning, Team Collaboration, and Training)
      Manages team assignments, project workflows, expected timelines, documentation, training, and organizational resources necessary to create software
      systems or software applications.

   Provenance Generation and Verification Tool 
      Generates and verifies SBOM information (i.e., software dependencies, configuration files, scripts, or source code) that is included in the
      produced software applications or systems.

   Regression Test Tool
      Provides tools to perform automated regression testing to verify that functional or security components haven't inadvertently broken prior
      functionality.

   Release Management System
      Manages the software release process (i.e., the planning, coordinating, notification, and distribution) of software applications, libraries, or packages.

   Requirements Management System
      Provides tools and processes to create, decompose, assign, and track, the requirements of a software application.

   Risk Management System
      Provides the processes and tools necessary to identify, prioritize, track, classify, and assess risks to the CI/CD pipeline and its components, software
      systems, or software applications. This also can create reports, mitigations, notifications, alerts, and dashboards to track the overall status of
      organizational, system, or application levels of risk for maintaining situational awareness for stakeholders.

   Runtime Signature Verification Tool
      Verifies the digital/cryptographic signature of runtime assets.

   SAST System
      Analyzes source code for defects, security vulnerabilities (i.e., SQL injection, cross-site scripting, buffer overflow, or leaked secrets or
      credentials). This can include code changes or other remediations; or can provide alerts or notifications to stakeholders.

   SCA System
      Provides tools for analyzing and tracking source code or open-source/commercially available software libraries to identify defects, software
      vulnerabilities, or licensing issues. This can include software patches, configuration changes, or other remediations; or can provide alerts or
      notifications to stakeholders.

   SCM System (e.g., Version Control, Commit Hooks, and Branch/Merge Protection)
      Manages the storage, retrieval, and controlled access of source code, software repositories, repository policies, code changes (i.e., commits, branches,
      tags, merge/pull requests, and forks). This can also provide version control and monitoring of changes to source code. Additional functionality
      includes commit hooks and branch/merge protections to provide automated control of security scans, lint tool, or merge/pull request approval for
      software repositories and source code.

   Secrets Management System
      Manages, protects, and maintains secrets (i.e., usernames, passwords, API keys, or configuration details) that are assigned to software applications or
      services for use in machine-to-machine integration (i.e., authentication, authorization, or configuration).

   Secret Scanner
      Scans for exposed secrets (i.e., certificate keys, credentials, API keys, and other sensitive variables) in source code or configuration files to
      prevent accidental disclosure.

   Security Monitoring System (e.g., Vulnerability Management, Incident Management, Security Information and Event Management (SIEM), and Security Orchestration, Automation, and Response (SOAR))
      Manages detection, analysis, categorization, and responds to security threats, vulnerabilities and compromises by providing tools to analyze event data,
      generate real-time alerts, automate investigation, implement remediation workflows, and provide ongoing visibility into the security posture of
      applications and infrastructure.

   Smoke Test Tool
      Provides the tools and scripts to verify that critical software system or application functionality is preserved and stable as source code or build
      artifacts are changed.

   Software Libraries (e.g., Internal and External)
      Consists of pre-written, reusable source code, or software packages that provide functionality to support requirement implementation and are
      incorporated into the software application build.

   Team Collaboration Tools
      Provides communication and coordinates between development, security, and operations teams to improve system reliability and security based on shared
      insights and feedback.

   Threat Modeling System
      Provides the tools and data necessary to identify and assess potential security threats (i.e., insider threats, bad actors, pipeline corruption, or
      exploited vulnerabilities). This can also provide the necessary reports and notifications to track organizational, system, or application levels of
      risks for stakeholders.

   Ticketing System
      Manages the tracking of tasks and bugs discovered in prior iterations of the DevSecOps lifecycle for software systems and software applications. This
      includes the creation, assignment, and resolution of tasks and roles (e.g., tickets, issues, or work items) to different groups (i.e., projects, teams,
      or individuals).

   Unit Test Framework
      Provides the tools and scripts to perform validation tests for individual components or functions of software systems or software applications in the
      develop, build and test phases. This is done to ensure that all components still work outside of the Build environment.

   Zero Trust Security System
      Overarching security architecture that enables robust authentication, authorization, policy assignment, policy enforcement, continuous monitoring, and
      segmentation. This includes access verification, implementation of least privilege, and validation of security posture for devices. This can create and
      maintain physical and/or logical perimeters for software systems and software applications to prevent unauthorized access to resources (e.g., user or
      service accounts, systems, networks, software applications, or facilities).