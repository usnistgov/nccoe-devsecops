Appendix C Collaborators and their Contribution
================================================

The organizations participating in this project submitted their capabilities in response to an open call in the Federal Register and entered into a CRADA with
NIST. Each collaborator provides products, services, and/or expertise relevant to the project. Each of these technology collaborators has described the relevant
products and capabilities they bring to this project in the following subsections.

The NCCoE does not certify, validate, or endorse products or services. We demonstrate the capabilities that can be achieved by using participants’ contributed
technology. Your organization’s information security experts should identify the products that will best integrate with your existing tools and IT system
infrastructure.

C.1. AMI
~~~~~~~~

AMI offers firmware for security, orchestration, and manageability solutions and enables compute platforms from on-premises, to the cloud, to the edge.

C.1.1. Meridian Firmware Management Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Meridian Firmware Management Service (FMS), a cloud-hosted solution, is a component of AMI’s firmware platform, designed to improve how Original Design
Manufacturers (ODMs) manage platform firmware lifecycles. As part of the broader Meridian platform, FMS’s role is to deliver a secure, scalable pipeline for
accessing and maintaining AMI firmware sources, allowing ODMs to port and customize firmware for their specific hardware platforms. The service exposes suites
of APIs to manage firmware sources, perform cryptographic signing, orchestrate automated test scripts, generate SBOM reports, and deploy validated firmware
directly to platforms.

C.1.2. Meridian Security Services: VMS and SBOM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Meridian Vulnerability Management Service (VMS) and SBOM Security Service under the cloud-based Meridian Security Services provides a framework for securing
the firmware supply chain across AMI, ODM, and Original Equipment Manufacturer (OEM) deliverables. By generating and continuously updating SBOMs for every
firmware build, the service provides visibility into embedded components, libraries, and third-party dependencies. This supports identification and assessment
of vulnerabilities tied to specific versions, track component provenance, and responses to emerging CVEs. For ODMs and OEMs, the service supports identification
and management of inherited risks from upstream firmware sources. Integrated with vulnerability databases and real-time threat intelligence, the service
supports automated alerts, risk scoring, and policy implementations.

C.2. Black Duck
~~~~~~~~~~~~~~~

Black Duck offers a portfolio of software security products and services that address application security needs in sectors such as financial services,
automotive, critical infrastructure, and cloud services. Black Duck, originally a division of Synopsys called the Software Integrity Group, officially separated
from Synopsys as an independent company and was rebranded as Black Duck.

C.2.1. Polaris Platform
^^^^^^^^^^^^^^^^^^^^^^^

The Black Duck Polaris™ Platform is an integrated, cloud-based application security testing solution for use by development and DevSecOps teams. Polaris brings
the Black Duck Coverity, Dynamic, and SCA security analysis engines together in a unified platform for risk identification and management. Risk classes
identified include hard-coded secrets, security and quality defects in proprietary code, weaknesses in IaC templates, vulnerabilities in software supply chains,
and deployment risks in web applications, single-page applications, and cloud-native APIs.

C.2.2. Black Duck SCA
^^^^^^^^^^^^^^^^^^^^^

Black Duck® SCA supports management of security, code quality, and license risks that come from the use of open source and third-party code in applications and
containers. Black Duck SCA is a software supply chain security and risk management solution capable of analyzing binary, SBOM, and source code present within
applications.

C.2.3. Black Duck Coverity
^^^^^^^^^^^^^^^^^^^^^^^^^^

Coverity® Static Analysis provides comprehensive code scanning to support software security, functional safety, and industry standards. Coverity facilitates
tracking and management of business coding standards. The Code Sight™ IDE plugin extends Coverity analysis to the developer desktop, enabling developers to find
and fix quality and security defects as they code.

C.2.4. Continuous Dynamic
^^^^^^^^^^^^^^^^^^^^^^^^^

Continuous Dynamic™ is a DAST solution that supports finding vulnerabilities in websites and applications. The DAST solution performs scans and testing of
entire application portfolios as opposed to performing targeted scans. Continuous Dynamic combines AI with expert security analysis.

C.2.5. Software Risk Manager (SRM) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Software Risk Manager™ is an application security posture management (ASPM) solution for supporting security and development teams in managing application
security at enterprise scale. Correlation, deduplication, and summarization of findings across manual and automated AST tools help prioritize high-impact fixes
based on risk. Software Risk Manager provides software risk assessment of components including custom code, third-party, and open source as well as related
components like APIs, containers, and microservices.

C.3. CyberArk Software
~~~~~~~~~~~~~~~~~~~~~~

CyberArk is a provider of Identity Security, centered on privilege controls, with a focus on protecting organizations against identity-based cyber attacks.
Privilege controls are applied to all identities—human and machine—with continuous threat detection and prevention across the identity lifecycle. CyberArk
supports Zero Trust and least-privilege with visibility so that identities can securely access approved resources in multiple locations from a single Identity
Security platform.

C.3.1. CyberArk Privilege Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Privilege Cloud is a SaaS-based privileged access management (PAM) solution that is used to help organizations secure, control, and monitor privileged
access across hybrid environments. It offers automated credential management, real-time session monitoring, and least-privilege enforcement through native,
isolated access. It includes secure tunnels, SSH session support, and integrations with platforms like ServiceNow.

C.3.2. CyberArk Endpoint Privilege Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Endpoint Privilege Manager supports least-privilege enforcement and blocking and containment of attacks at the endpoint. A combination of Endpoint
Privilege Management, Privilege Threat Protection, and Application Control stops support-containment of damaging attacks at the point of entry. These protection
technologies are deployed as a single agent for desktops, laptops, and servers running Windows, Windows Server, macOS, or Linux.

C.3.3. CyberArk Code Sign Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Code Sign Manager is a centralized, policy-driven solution for securing enterprise code signing processes by safeguarding private keys in secure
hardware or software modules (HSMs or CM-SH), enforcing role-based access, and enabling audit-ready workflows. It combats key sprawl and unauthorized usage by
avoiding private keys from leaving the secure environment, while allowing developers to sign code from any location without direct access to the keys. The
platform supports timestamping, certificate lifecycle management, and integration with CI/CD pipelines. With upcoming SaaS deployment options and compatibility
across Windows, Linux, and macOS environments, Code Sign Manager is designed to support software supply chain integrity and trust.

C.3.4. CyberArk Secrets Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Secrets Hub is a SaaS solution for providing centralized visibility and control over secrets stored in native cloud provider vaults such as AWS Secrets
Manager, Azure Key Vault, and GCP Secret Manager. It supports security team discovery, monitoring and management of secrets across multi-cloud environments with
a goal of avoiding disruption of developer workflows or code changes. Secrets Hub acts as a bridge between CyberArk Privilege Cloud and cloud-native secret
stores. It supports automated onboarding, analytics for unused or unrotated secrets, and secure synchronization of credentials from Privilege Cloud to cloud
vaults.

C.3.5. CyberArk Conjur Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Conjur Cloud is a SaaS-based, cloud-agnostic secrets management solution designed to secure non-human access to credentials across dynamic,
multi-cloud, and hybrid environments. It provides centralized control, auditability, and policy enforcement for secrets used by applications, containers, and
DevOps tools. Conjur Cloud integrates with CyberArk Privilege Cloud and Certificate Manager, supports secure secret distribution via Conjur Cloud Edge, and
enables certificate issuance through integrations with CAs. It addresses the “secret zero” problem by avoiding hardcoding or exposure of secrets.

C.3.6. CyberArk Workload Identity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Workload Identity is a cloud-native solution designed to secure machine-to-machine authentication across dynamic, multi-cloud, and hybrid environments.
It issues short-lived, cryptographically verifiable identities to workloads, such as containers, VMs, and serverless functions, without relying on static
secrets, enabling secure workload-to-workload communication. Built on standards like SPIFFE/SPIRE, it integrates with CyberArk Conjur and Secrets Hub.

C.3.7. CyberArk Certificate Manager SaaS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Certificate Manager SaaS is a cloud-native solution designed to secure machine identities across dynamic, multi-cloud, and hybrid environments. It
automates the discovery, issuance, renewal, and revocation of SSL/TLS certificates to eliminate outages and ensure secure communication between services. It
enables automated, policy-based certificate management to eliminate manual errors. It is built to integrate with certificate authorities, cloud providers,
DevOps toolchains, and enterprise platforms to enforce zero-trust principles, eliminate certificate sprawl, and support consistent policy enforcement across
distributed systems.

C.3.8. CyberArk Certificate Manager (Self-Hosted) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CyberArk Certificate Manager (Self-Hosted) is an enterprise-grade solution designed to secure machine identities across dynamic, multi-cloud, and hybrid
environments. It provides control over the discovery, issuance, renewal, and revocation of SSL/TLS certificates to reduce outages and enable secure
service-to-service communication. It is built to integrate with certificate authorities, cloud infrastructure, DevOps tools, and enterprise systems to support
zero-trust initiatives, minimize certificate sprawl, and implement consistent policies across environments. It centralizes governance, detailed audit logs, and
customizable workflows.

C.4. Dell Technologies
~~~~~~~~~~~~~~~~~~~~~~

Dell Technologies provides infrastructure designed to enable organizations to build and protect information and embed security throughout the product or
application lifecycle with the objective of products and applications being built securely and remain secure. Dell’s security program includes analysis
activities such as threat modeling, static code analysis, and security testing to discover and address security defects throughout the development lifecycle.

Dell's baseline security capabilities are designed to meet customers’ security objectives and policy requirements including an internal business readiness
review process and internal security assessments of products or applications, to support Dell’s Secure Development Lifecycle (SDL).

C.5. DigiCert
~~~~~~~~~~~~~

DigiCert® provides high-assurance digital certificates and software to securely store and manage PKI and DNS. DigiCert solutions are designed to provide digital
trust for web TLS/SSL, identity, authentication, and encryption for Internet of Things (IoT)X, code and content signing, email, Post-Quantum Cryptography, and
DNS.

C.5.1. DigiCert Software Trust Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DigiCert® Software Trust Manager centralizes code signing governance to help companies comply with regulations. It securely manages the code signing certificate
lifecycle, including auto-renewing and auto-rekeying, plus certificate and keypair storage in cloud-based FIPS 140-2 Level 3 HSMs.

Software Trust Manager gives organizations granular control over team, and role-based access, privileges, policy, certificate and keypair templates, and
workflows, all with signing backed by Private or Public (Internal) PKI. Scanning for vulnerabilities, malware and license issues, signing code and software
artifacts, such as SBOMs, help protect the software supply chain.

With native integrations, APIs, and CLIs, DigiCert Software Trust Manager connects to modern CI/CD and development platforms, allowing automation to speed
software delivery and reduce manual delays and errors.

C.6. Endor Labs
~~~~~~~~~~~~~~~

Endor Labs is an AppSec platform for AI and open source-driven software development. Endor Labs offers code reviews, static analysis, risk-based prioritization,
and efficient remediation in a single, connected view. Its products cover open source, AI-generated and human-written code, and support flexible policies and
APIs. The endorctl client application provides access to the capabilities described below.

C.6.1. Reachability-Based SCA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Endor Labs uses deep program analysis to build a call graph of applications, showing whether vulnerable code is reachable instead of just present. Upgrade
Impact Analysis steers developers toward safe upgrades or, when upgrades are risky, applies minimal and verifiable patches that fix issues without breaking
functionality. The platform also uncovers transitive dependencies, AI models, and GitHub Actions. It centralizes inventories and monitors every item for more
than 150 risk factors across license, code quality, maintainability, and malicious software to prevent supply chain attacks. A native MCP server brings that
same intelligence straight into AI coding assistants, and as AI accelerates the flow of code and dependencies, this blend of precise reachability analysis,
in-workflow remediation, and AI code governance cuts noise, sustains developer trust and helps teams meet remediation SLAs.

C.6.2. Endor Code (SAST + Secret Scanning) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Endor Code brings SAST into the same platform that powers SCA, container scanning, and secrets detection, so it is not necessary to juggle separate tools, UIs,
or policy engines. Endor Code ships with easily customized curated rules by a team of security researchers. Findings are actionable and backed by code-level
context to inform developers regarding what triggered an alert and what to do next. Endor Code is managed through a unified policy engine.

C.6.3. Container Scanning
^^^^^^^^^^^^^^^^^^^^^^^^^

Endor Labs integrates container scanning directly with SCA to provide a single view of vulnerability risk across application code and container images. False
positives are reduced by correlating findings across both scans and extending reachability analysis to containers. Layered analysis identifies exactly which
part of the image introduced a vulnerability, base image vs. app layer to enable assigning a fix to the right team. Combined with consolidated SBOMs and CI/CD
policies for trusted base images supports remediation, ownership, and streamlined security from one platform. Endor Labs enhances software supply chain security
by providing transparent mechanisms for signing and verifying software artifacts.

C.6.4. Endor Patches
^^^^^^^^^^^^^^^^^^^^

Endor Patches are backported security patches that permit vulnerability fixes without an upgrade. Endor extracts and backports vetted open-source patches from
newer versions and applies them directly to the desired version. These minimal patches are scoped only to the security fix and tested for compatibility. These
can be applied manually or automatically during builds across many repos. Patches are transparent and verifiable with reproducible builds and full SBOM
reporting, and, with reachability analysis and Upgrade Impact Analysis, can support decisions regarding when patching is the right call and when a safe upgrade
is possible.

C.6.5. AI Code Security Review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AI Security Code Review from Endor Labs detects material changes to an application’s security architecture. A material change might include the introduction of
a new API endpoint, alteration to authentication methods, collection of additional types of personally identifiable information (PII), or changes to the
cryptographic library for SSL, as examples. Endor Labs uses a multi-agent architecture for AI Security Code Review. The AI agents mimic the way a human
application security engineer would approach a secure code review by playing a distinct role in the analysis process. The AI agents work in sequence to analyze
every PR, identify security-relevant changes, and then categorize and prioritize them. Together, the agents form a layered reasoning system that moves from
“what changed” to “why it matters” for security.

C.7. GitLab
~~~~~~~~~~~

GitLab provides a DevSecOps platform in a single application designed to constitute the entire software development lifecycle—from source code management and
CI/CD to issue tracking, security, testing, deployment, and monitoring. The platform can be used as either a traditional SaaS solution, a single-tenant
dedicated SaaS offering (with a FedRAMP option), or via self-managed and cloud-agnostic instances that customers control and operate (connected to the Internet
or not). GitLab Duo adds advanced AI features to each step of the SDLC. Customers can swap one or more built-in features out.

C.7.1. The GitLab Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^

GitLab is an integrated DevSecOps platform that covers all stages of the software development lifecycle in a single application with a unified data store. For
planning, it includes issue creation/tracking, milestones to organize work, boards for project management, roadmaps for strategic planning, and requirements for
management capabilities. The development core is Git-based source code management with merge requests for code review and a Web IDE. GitLab’s CI/CD pipelines
automate building, testing, and packaging code, supporting multiple languages and frameworks and generating SBOMs. Automated testing is integrated throughout,
including unit tests, integration tests, code quality checks, and accessibility testing. Security scanning throughout the pipeline includes SAST, DAST,
dependency scanning, and container scanning. A built-in package registry supports various formats and container registry for Docker images featuring
container-specific SBOMs. GitLab allows automated deployment to multiple environments, including Kubernetes integration and support for gradual rollouts.
Application performance monitoring, error tracking, and incident management help teams maintain production systems. Integrated logging and tracing provide
visibility into application behavior.

C.7.2. GitLab Duo (AI) 
^^^^^^^^^^^^^^^^^^^^^^^

GitLab Duo is GitLab’s suite of AI features designed to enhance developer productivity throughout the software development lifecycle, integrating AI
capabilities directly into the GitLab platform rather than requiring separate tools or plugins. Key features include AIcode completion and generation that
understands context across files and projects, conversational AI chatting for answering questions about code, GitLab features, and development best practices,
quick summarization of sections of code, issues, merge requests, epics or discussion threads, vulnerability explanations for security issues, including
remediation guidelines, root cause analysis for failed pipelines, automated suggestions during code reviews, automatic creation of unit tests based on existing
code, and an overarching umbrella of privacy protection so that code and queries are not retained or used to train future models.

C.8. Google
~~~~~~~~~~~

Alphabet Inc. (Google) is an American multinational technology corporation. Google specializes in internet-related services and products, which include online
advertising technologies, a search engine, cloud computing (Google Cloud), software, and hardware. Google’s portfolio of products and services includes
categories such as search, advertising, operating systems (Android, Chrome OS), cloud platforms (Google Cloud), threat intelligence (Mandiant), video sharing
(YouTube), mapping (Google Maps), artificial intelligence (Google Deep Mind), and a range of consumer electronics like smartphones (Pixel) and smart home
devices. Google is also heavily involved in research and development, constantly involved in areas like autonomous driving (Waymo) and life sciences (Calico).

C.8.1. Cloud Workstations
^^^^^^^^^^^^^^^^^^^^^^^^^

Cloud Workstations is a managed development environment. It allows for running inside a VPC perimeter or can apply a “no source code on local devices.”
Workstations can run inside any editor, including IntelliJ IDEA, PyCharm, Rider, and CLion through JetBrains Gateway, as well as Posit Workbench. It also
provides a managed experience using predefined or custom containers to specify environment configuration, such as pre-installed tools, libraries, IDE
extensions, preloaded files, and start-up scripts. Finally, Cloud Workstations supports Gemini Code Assist, which provides AI assistance to developers, such as
auto code completion, code generation, and chat.

C.8.2. Google Cloud Build
^^^^^^^^^^^^^^^^^^^^^^^^^

Google Cloud Build is Google’s serverless CI/CD platform. Cloud Build supports fast builds via access to machines connected via Google’s global network and
allows running of builds on high-CPU VMs and to cache source code, images, or other dependencies. Builds can be run on default or private pools based on
networking and scaling needs. Default pool lets you run builds in a secure, hosted environment with access to the public internet. Private pools are private,
dedicated pools of workers offering you greater flexibility over the build environment with greater concurrency, and the ability to access resources in a
private network. Cloud Build features native integration with other Google CI/CD products, including Google Kubernetes Engine, Cloud Run, App Engine, Cloud
Functions, and Firebase. Finally, Cloud Build automatically generates provenance metadata and verification for container images and language packages at build
time to trace binary to the source code and prevent tampering.

C.8.3. Artifact Registry and Artifact Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Artifact Registry, Google’s universal package manager, permits central storage of artifacts and build dependencies as part of an integrated Google Cloud
experience. Artifact Registry natively supports storage of Docker container images, language packages (including Python, Javascript, Go, etc.), OS packages
(including APT and RPM), and generic package formats. In addition to local storage, Artifact Registry provides remote repositories to cache dependencies from
upstream public sources to provide greater control over the artifacts and their metadata, as well as virtual repositories to group remote and private
repositories behind a single endpoint. Artifact Registry natively integrates with Artifact Analysis, which provides vulnerability scanning and metadata
generation for containers on Google Cloud. Artifact Analysis allows for continuous scanning of artifacts in Artifact Registry, as well as On-Demand Scanning for
local artifacts. Artifact Analysis further allows for the generation of SBOM.

C.8.4. Binary Authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Binary Authorization is a service on Google Cloud that provides centralized software supply-chain security for applications that run on Google Kubernetes Engine
(GKE) and Cloud Run. Binary Authorization enforcement can be configured to apply that images that are being deployed conform with a policy that users define.
Images that conform with the policy are allowed to be deployed; otherwise, they are disallowed from being deployed. Alternatively, users can configure
continuous validation with check-based platform policies to periodically monitor that container images associated with running Pods conform to a policy that
they define. If images don’t conform with the policy, CV produces log entries in Cloud Logging.

C.8.5. Cloud Deploy
^^^^^^^^^^^^^^^^^^^

Cloud Deploy creates deployment pipelines for GKE, Cloud Run, and other supported runtimes. It allows defining releases and progressing them through
environments, such as test, stage, and production. Cloud Deploy provides one-step promotion and rollback of releases via the web console, CLI, or API. Built-in
metrics enable insight into deployment frequency and success. Furthermore, it is fully integrated with GKE, Cloud Run, and Anthos deployment platform available,
which allows locking down release progression via IAM, monitor release events with Cloud Logging, and achieve traceability with Cloud Audit Logs. It also can be
integrated with DevOps tools, such as CI and ticketing. Cloud Deploy brings Skaffold to pipelines, which, in unison with Cloud Code, brings pipeline parity
across dev and CI/CD.

C.8.6. Google Kubernetes Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Google Kubernetes Engine is a scalable, automated Kubernetes service. GKE supports up to 65,000 nodes per cluster, which allows for model training, serving,
inference, conducting ad hoc research, and managing auxiliary tasks. GKE provides fully automated cluster life cycle management, pod and cluster autoscaling,
cost visibility, and automated infrastructure cost optimization, plus management, governance, security, and configuration for multiple teams and clusters with
unified console experience and integrated service mesh. GKE integrates natively with the suite of Google Cloud products, allowing for Google Cloud Build and
Cloud Deploy to deploy directly to the GKE cluster.

C.8.7. Cloud Run
^^^^^^^^^^^^^^^^

Cloud Run allows users to run apps or websites on a managed platform, while allowing writing of code using a choice of language, framework, and libraries,
package it up as a container, and deploy it with one command. Cloud Run automatically scales containers up and down from zero, and only charges when code is
running. Cloud Run can also automate getting to production, using buildpacks that enable direct deployment from source without having to install Docker on your
machine. Builds can be automated and code can be deployed whenever new commits are pushed to a given branch of a Git repository. Finally, Cloud Run supports AI
inference workloads by providing access to NVIDIA L4 GPUs.

C.8.8. Security Command Center
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Security Command Center (SCC) delivers security for Google Cloud environments with solutions for managing cloud risks and protecting AI workloads. SCC allows
users to discover and catalog AI assets, including the use of models, applications, and data, guard against prompt injection, jailbreak, data loss, malicious
URLs, and offensive content, and defend AI systems against AI-specific threats and risks. It provides support to discover malicious and suspicious activity in
Google Cloud services, including Compute Engine, GKE, BigQuery, CloudRun, and more. Finally, SCC automatically scans the user cloud environment to identify
cloud misconfigurations and software vulnerabilities that could lead to compromise without having to install or manage agents. High-risk findings are presented
on the Security Command Center risk dashboard, to permit users to know which issues to prioritize.

C.8.9. deps.dev
^^^^^^^^^^^^^^^

deps.dev is Google’s open-source data warehouse, designed to enhance the understanding, security, and health of the open-source software supply chain. It
functions by collecting, processing, and aggregating data on open-source artifacts, making it universally accessible and useful, to help developers better
understand the structure, construction, and security of open-source software packages. The service can be used via the deps.dev website, API or BigQuery
datasets.

C.9. IBM
~~~~~~~~

International Business Machines Corporation (IBM) is an American multinational technology corporation. IBM produces computer hardware, middleware, and software,
and provides hosting and consulting services spanning areas from mainframe computing to nanotechnology. IBM is also a research organization and has a diverse
portfolio of products and services that include the categories of cloud computing, AI, commerce, data and analytics, IoT, IT infrastructure, mobile, digital
workplace, and cybersecurity.

C.9.1 IBM Cloud and DevSecOps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IBM Cloud is designed to permit organizations in regulated industries to deliver software rapidly while maintaining security controls and continuous audit
readiness. IBM Cloud offers a reference implementation for a secure, integrated software supply chain that enables DevSecOps by embedding security across the
software lifecycle.

The platform combines security automation, policy enforcement, and auditability. The platform orchestrates activities including vulnerability scanning, artifact
signing, SBOM generation and assessment, GitOps-based deployments, change tracking, reporting, and code remediation. Deviations from policy are tracked and
documented, and change requests include rationale and approvals to support governance transparency. Evidence for each control, including build logs and test
results to vulnerability findings, remediation actions, and release artifacts is automatically captured and stored in S3‑compatible object storage.

C.9.2 IBM Cloud Continuous Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IBM Cloud Continuous Delivery is a fully managed, hosted service for creating toolchains from templates, streamlining build, test, and release workflows through
integrated Git repositories, issue tracking, and Tekton‑based pipeline orchestration. Pipelines are declarative, reusable, and portable, enabling teams to
standardize delivery processes across applications and environments. The service includes Code Risk Analyzer for early source composition analysis, SBOM
generation, and dependency checks, as well as DevOps Insights for aggregating build, test, and scan data into quality and governance dashboards with policy
gates.

With IBM Cloud Continuous Delivery, IBM operates the complete pipeline runtime in order to provide scalability and availability while pipeline executions run
within Kata Containers to deliver strong and lightweight isolation in multi‑tenant environments. For hybrid scenarios, private workers can be deployed into
customer‑managed networks—including on‑premises, private cloud, and isolated environments, allowing pipelines to securely access internal systems and deploy
workloads across heterogeneous infrastructures.

C.9.3 IBM Cloud Container Registry and Vulnerability Advisor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IBM Cloud Container Registry provides a managed, hardened repository for storing and promoting container images across environments. The registry integrates
with IBM Cloud Vulnerability Advisor to perform continuous security scanning of images, analyzing operating system packages and application dependencies against
known vulnerabilities. Findings are presented with risk context and remediation, enabling rapid response.

Policies can be applied to prevent images that exceed defined risk thresholds from advancing to staging or production, helping ensure that only approved
artifacts are deployed. Image signing and integrity verification further strengthen the chain of custody, providing assurance that artifacts have not been
altered and that provenance can be demonstrated.

C.9.4 IBM Cloud Kubernetes Service and Red Hat OpenShift Services 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For deployment and scaling of cloud‑native workloads, IBM Cloud Kubernetes Service (IKS) and Red Hat OpenShift on IBM Cloud (ROKS) provide managed container
orchestration platforms. These services support capabilities such as role‑based access control, network policies, cluster hardening options, and integration
with identity and access management, IBM Cloud Secrets Manager, and IBM Cloud Key Protect.

Both services are intended for GitOps-based delivery models, where declarative manifests define the desired state and operational changes are
version‑controlled, reviewed, and auditable. Admission controls and policy engines can prevent workloads that do not meet the requirements from being deployed,
ensuring that runtime environments maintain the same governance rigor as build and packaging stages.

C.9.5 IBM Cloud Secrets Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IBM Cloud Secrets Manager provides centralized, encrypted storage for sensitive data such as API keys, passwords, tokens, and certificates. Secrets are
protected both in transit and at rest, and access can be precisely scoped to specific applications, services, or pipeline stages.

C.9.6 IBM Cloud Key Protect
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cryptographic controls and artifact integrity are supported through IBM Cloud Key Protect, a managed key management service that enables organizations to
generate, store, rotate, and control encryption keys. Keys can be used for data encryption, artifact signing, and protection of sensitive information across
pipelines and applications.

Key lifecycle operations are centrally governed, and customer‑managed keys support data protection and sovereignty requirements. When combined with artifact
signing, SBOMs, and provenance metadata, Key Protect helps organizations demonstrate the origin, integrity, and contents of software artifacts throughout the
supply chain.

C.9.7 IBM Cloud Object Storage (S3‑Compatible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IBM Cloud Object Storage provides highly available, scalable storage for logs and artifacts. Build outputs, SBOMs, test results, pipeline logs, vulnerability
reports, change records, and deployment manifests can be preserved using versioning and immutability controls.

Lifecycle policies help balance retention requirements with cost management, while maintaining rapid access to critical evidence. With a centralized repository
for artifacts, organizations can respond to audits efficiently and present traceable records demonstrating control adherence across the software delivery
lifecycle.

C.10. Microsoft and GitHub Advanced Security (GHAzDO) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft and GitHub offer a comprehensive DevSecOps ecosystem designed to integrate security into all phases of the software development lifecycle. At the core
GitHub Advanced Security for Azure DevOps (GHAzDO) includes CodeQL for static code analysis, secret scanning, and dependency vulnerability detection. These
tools are designed to enable early identification and remediation of security issues, embodying the “shift-left” security principle.

Azure DevOps (AzDO) complements GitHub by providing secure CI/CD pipelines, artifact provenance, and SBOM generation. Features like GitHub Actions and Azure
Policy integration allow automated implementation of security and policy controls. GitHub Copilot further enhances developer productivity with AI-assisted
coding while maintaining secure coding practices.

Azure Entra ID provides identity and access management, with granular RBAC, multifactor authentication, conditional access policies, and anomaly detection.
Azure Key Vault secures secrets, while Azure Policy and Defender for Cloud apply policy and monitor security posture across environment.

C.10.1. Azure Container Registry (ACR) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure Container Registry (ACR) is a managed Docker container registry service by Microsoft Azure. It is intended to enable developers to store, manage, and
deploy container images and artifacts securely. ACR integrates with Azure Kubernetes Service (AKS), Azure DevOps, and GitHub Actions, supporting
geo-replication, private endpoints, and content trust for secure, efficient CI/CD workflows.

C.10.2. Azure DevOps (AzDO) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure DevOps (AzDO) is Microsoft’s end-to-end platform for managing the software development lifecycles, integrating planning, development, testing, delivery,
and monitoring. The core services include Azure Boards for agile planning and tracking, Azure Repos for version control, Azure Pipelines for CI/CD automation,
Azure Test Plans for quality assurance, and Azure Artifacts for package management.

AzDO supports hybrid and multi-cloud deployments, integrates with GitHub, and enables IaC using Bicep, ARM templates, and Terraform. It also facilitates secure
software supply chains through component governance and vulnerability scanning during build and release pipelines. Organizations can customize workflows using
extensions and manage access via Microsoft Entra ID (formerly Azure AD).

Azure Artifacts is a service within AzDO that enables teams to create, host, and share packages such as NuGet, NPM, Maven, PyPi, and Universal Packages. It
supports versioning, retention policies, and upstream sources, allowing secure and scalable package management. Integrated with CI/CD pipelines, it helps
maintain reliable and traceable builds.

AzDO extensions are add-ons that enhance the functionality of AzDO by integrating third-party tools or adding custom capabilities; they support tasks like test
management, security scanning, deployment automation, and reporting. Available through the Visual Studio Marketplace, these extensions help teams tailor AzDO to
fit their workflows and DevSecOps needs.

C.10.3. Azure Entra ID
^^^^^^^^^^^^^^^^^^^^^^

Azure Entra ID is designed to provide secure identity and access management across the software development lifecycle. It enables conditional access,
multifactor authentication, and least-privilege enforcement for developers, pipelines, and workloads. With workload identity federation, DevOps tools like
GitHub Actions and Azure Pipelines can be able to securely access Azure resources without storing secrets. Entra ID also supports just-in-time access, access
reviews, and role-based access control to minimize exposure and apply governance. Integration with Microsoft Defender for Cloud and Microsoft Sentinel allows
real-time monitoring and automated response to identity-related threats. These capabilities help embed security into DevOps workflows.

C.10.4. Azure Key Vault (AKV) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure Key Vault (AKV) is designed to enable DevOps teams to secure secrets, keys, and certificates. By centralizing sensitive information, it eliminates
hard-coded credentials and reduces security risks across pipelines. Integrated with Azure DevOps and automation tools, Key Vault enables secret rotation, access
control, and policy implementation. Its robust encryption and identity-based access provide auditable security to deployments, accelerate delivery, and maintain
enterprise-grade protection for cloud-native applications.

C.10.5. Azure Managed DevOps Pool (MDP) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure Managed DevOps Pools (MDP) are a managed, scalable solution for running Azure DevOps pipelines without needing to independently manage infrastructure.
Hosted in Microsoft’s Azure subscription, these pools provide agent provisioning, maintenance, and pre-configured environments for CI/CD workloads. They support
custom VM images, caching, and long-running jobs up to 48 hours and support complex enterprise builds.

Under Azure Dev Center, the MDP centralizes preconfigured, secure compute, and build images for projects, governed by policy and RBAC. Teams can draw
standardized environments on demand, with elastic scaling, cost controls, and secure baselines. Automation via pipelines and APIs provisions, updates, and
retires resources, and supporting consistent developments.

C.10.6. Azure Privileged Identity Management (PIM) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure Privileged Identity Management (PIM) delivers just in time, time bound, and approval based privileged access across Microsoft Entra ID, Azure, and
Microsoft 365 resources. It reduces standing administrator permissions, applies MFA, captures detailed audit logs, and supports access reviews to ensure least
privilege governance. PIM offers automated role activation workflows and robust monitoring.

C.10.7. Azure Sentinel
^^^^^^^^^^^^^^^^^^^^^^

Azure Sentinel, now known as Microsoft Sentinel, is a scalable, cloud-native security information and event management (SIEM) and security orchestration,
automation, and response (SOAR) solution. It enables organizations to collect, analyze, and respond to security data across hybrid and multi-cloud environments.
Sentinel uses built-in AI and Microsoft threat intelligence to detect and investigate threats in real time, reducing alert fatigue and enabling faster incident
response. It supports data ingestion from a wide range of sources, including Microsoft 365, Azure, AWS, and third-party platforms.

C.10.8. Bicep and Azure Resource Manager (ARM) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure Resource Manager (ARM) is a deployment and management service for consistent provisioning and management of Azure resources. It uses JSON-based templates
to define infrastructure, enabling repeatable, declarative deployments with support for dependencies, role-based access control, and policy enforcement.

Bicep is a domain-specific language (DSL) that simplifies authoring ARM templates in a concise, readable syntax while maintaining full ARM compatibility. Bicep
supports modularization, symbolic references, and tooling integration with Visual Studio Code and Azure CLI, making it easier to manage complex cloud
environments.

C.10.9. GitHub Advanced Security (GHAS) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GitHub Advanced Security (GHAS) is a native, developer-centric security suite integrated into GitHub Enterprise. It provides proactive protection through
features like Code Scanning (powered by CodeQL), Secret Scanning, and Dependency Review. These tools are designed to help developers identify and fix
vulnerabilities directly in pull requests, with AI suggestions and minimal context switching.

GHAS is designed for extensibility, and diverse DevSecOps workflows. GHAS is offered as two standalone products—GitHub Secret Protection and GitHub Code
Security.

GHAS also integrates with Azure DevOps called GitHub Advanced Security for Azure DevOps (GHAzDO), to enable unified visibility and remediation across platforms.

C.10.10. GitHub Copilot
^^^^^^^^^^^^^^^^^^^^^^^

GitHub Copilot is becoming a DevSecOps enabler. It blends AI-assisted development with secure software practices. At its core, Copilot acts as an AI pair
programmer, with real-time code suggestions, test generation, and documentation support across popular IDEs like Visual Studio Code, JetBrains, and NeoVim. For
DevSecOps, Copilot integrates with GitHub Actions and GitHub Advanced Security to apply security checks, scan for secrets and vulnerabilities, and support SBOM
generation directly within CI/CD pipelines.

The new “Agent Mode” allows developers to interact with Copilot using natural language to execute predefined tasks—such as provisioning infrastructure with
Bicep templates or validating security policies. Copilot Spaces, launched in May 2025, grounds Copilot’s responses in curated project-specific context,
including code, documentation, and custom instructions. Copilot’s reduces context switching, supports accelerated secure coding, and supports developers’
development of security best practices.

C.10.11. IDEs – Visual Studio and Visual Studio Code (VS Code) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Visual Studio is Microsoft’s integrated development environment (IDE) for building, debugging, and deploying applications across platforms including Windows,
web, cloud, and mobile. It supports multiple programming languages like C#, C++, Python, and JavaScript, and offers features such as IntelliSense, live unit
testing, and integrated Git support.

Visual Studio Code (VS Code) is a lightweight, open-source code. It supports a wide range of languages and frameworks through extensions, includes Git
integration, and offers features like IntelliCode, debugging, and remote development. It can be used for web and cloud-native development.

C.10.12. Microsoft Defender for Cloud (MDC) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microsoft Defender for Cloud is a cloud-native application protection platform (CNAPP) for securing multi-cloud and hybrid environments across the application
lifecycle—from code to runtime. It combines Cloud Security Posture Management (CSPM), Cloud Workload Protection (CWP), and DevSecOps capabilities for unified
visibility, threat detection, and proactive risk mitigation. CSPM features include agentless vulnerability scanning, data-aware posture insights, and advanced
threat hunting via the Cloud Security Graph. CWP provides protection to virtual machines, containers, databases, storage, APIs, and AI workloads with
workload-specific threat detection and adaptive controls. Defender for Cloud also integrates with Microsoft Threat Intelligence to detect anomalies and
prioritize remediation.

Microsoft Defender for Cloud supports third-party integrations to extend security visibility and response across hybrid and multi-cloud environments. It
connects with tools like ServiceNow, Splunk, and Palo Alto Networks to share threat intelligence, automate incident response, and more.

C.10.13. Microsoft SBOM Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microsoft SBOM Tool supports the creation and validation of SBOMs to support supply chain security. It supports industry standards like SPDX to enable
developers to generate accurate SBOMs for open-source and proprietary components. Integrated with CI/CD pipelines, the tools are designed to help organizations
meet regulatory requirements, improve transparency, and reduce risk by identifying vulnerabilities early. Its automation capabilities are designed to make SBOM
management more efficient and scalable across DevSecOps workflows.

C.10.14. Notary Project
^^^^^^^^^^^^^^^^^^^^^^^

Notary Project is a CNCF initiative to establish standards for signing and verifying OCI artifacts such as container images, SBOMs, and Helm chartsin support of
software supply chain security. It includes tools like Notation for signing and Ratify for policy-based verification. Microsoft contributes by integrating
Notary Project with Azure Key Vault, Trusted Signing, and Azure Kubernetes Service for automated certificate management and enforcement of signature
verification at deployment.

C.11. NextLabs
~~~~~~~~~~~~~~

NextLabs®, Inc. provides zero trust data-centric security software and services to protect data across applications, databases, files or file
repositories—on-premises or in the cloud. NextLabs’® dynamic authorization technology and attribute-based zero trust policy platform supports enterprise
identification and protection of sensitive data, monitor and control access to the data, and prevent violations. NextLabs software is designed to prevent
unauthorized access and automates implementation of security controls and policies to enable secure collaboration and information sharing across the extended
enterprise. NextLabs Zero Trust Data Security is a suite of access enforcement and data protection products driven by a zero-trust policy platform. The Suite
consists of the CloudAz Zero Trust Policy Platform and three lines of Policy Enforcers:

1. Application Enforcer to secure applications, externalize entitlement, protect application data, and enforce access based on least privilege principles

2. Data Access Enforcer to secure all access to critical data independent of application

3. SkyDRM to provide persistent protection of digital information stored in files at rest, in use, and in motion

C.11.1. NextLabs CloudAz Zero Trust Policy Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CloudAz is a centralized policy management platform with a dynamic authorization policy engine that centralizes administration of policy and employs zero-trust
principle to enforce data-centric security measures and policy-based access control in real-time. The CloudAz policy engine provides the foundation for
automating least privilege access, securing applications with Attribute Based Access Control (ABAC), and ensuring proper protection and security controls on
data. It integrates with existing identity management solutions and provides comprehensive logging and reporting capabilities to simplify policy verification.

C.11.2. NextLabs Policy Enforcer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sections below describe the details of NextLabs’ Policy Enforcer.

C.11.2.1. Application Enforcer – Externalized Authorization Management & ABAC
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

NextLabs’ Application Enforcer is a collection of enforcers that work natively with enterprise applications through built-in awareness of the application data
model and business process workflow. Application Enforcer augments an application’s underlying security model, providing an extra layer of control for
organizations with extensive security and policy requirements, without the need for custom coding. The solution also enforces Attribute-Based (ABAC) and
Policy-Based Access Control (PBAC) in real-time based on the values of the subject, data, and environmental attributes, as well as externalizing authorization
via a zero-trust policy engine to simplify access management, strengthen application security, and eliminate authorization siloes.

C.11.2.2. Data Access Enforcer – Secure Global Data Access
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Applying Zero Trust principles to implement robust data access security across applications, Data Access Enforcer (DAE) supports privacy and protection of data
with `logical data segregation <https://www.nextlabs.com/products/data-access-enforcer/what-is-data-segregation/>`__, record-level filtering, field-level data
masking, and dynamic data obfuscation. It controls access to data through fine-grained attribute-based policies that are dynamically enforced at runtime,
regardless of how the data is being accessed. DAE provides dynamic data-level security controls and fine-grained data access governance independent of services,
applications, UI, and API, while supporting any commercial-off-the-shelf application with a single set of policies.

C.11.2.3. SkyDRM – Enterprise Digital Rights Management
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

SkyDRM provides persistent control of access and usage of digital information stored in files throughout its lifecycle—at rest, in use, and on the move using
attribute-based policies. Attribute-based policies dynamically grant permissions for specific actions, such as viewing, editing, copying, forwarding, printing,
and extracting content, based on the recipient’s identity. The enforcer is file type agnostic and provides support for federated identity to enable
cross-enterprise collaboration. Any file type can be protected and accessed from any device to ensure secure collaboration across devices, data centers, apps,
cloud services, and on-premises. Users can access protected files through a web browser, mobile clients, or their native applications.

C.12. Palo Alto Networks
~~~~~~~~~~~~~~~~~~~~~~~~

Palo Alto Networks provides a portfolio of security services and platforms. The company has expanded its offering from Next-Generation Firewalls (NGFWs) to
address security across network, cloud, and endpoint environments. Its products and services include securing infrastructure, protecting against cyber threats,
and managing security operations, with a focus on cloud-native security and the integration of artificial intelligence for threat detection and response.

C.12.1. Cortex Cloud Security Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Cortex platform provides security orchestration and automation capabilities. Within a DevSecOps framework, it functions by integrating with the various
security and development tools used throughout the CI/CD pipeline. Its capabilities extend from development to deployment and runtime. The platform integrates
with CI/CD pipelines and development tools to scan IaC templates, source code, and container images for vulnerabilities and security issues. Once deployed, it
provides Cloud Security Posture Management (CSPM) to monitor for misconfigurations in the cloud environment and Cloud Workload Protection (CWPP) to secure
running hosts, containers, and serverless functions against threats. When a security scanner or monitoring tool detects a potential vulnerability or
misconfiguration, the platform triggers automated playbooks. These playbooks execute a sequence of actions, such as creating a detailed ticket in a project
management system, notifying the appropriate development team via communication platforms, and enriching the alert with contextual data to facilitate a faster
remediation process.

C.13. Sagittal AI
~~~~~~~~~~~~~~~~~

Sagittal AI is an early-stage, VC-backed startup focused on collaboration between humans and AI. Rather than forcing humans to adapt to AI, Sagittal designs AI
systems to adapt to humans. By integrating AI workflows with existing tools, processes, and job functions, Sagittal supports reducing workload and enhanced team
AI capabilities.

C.13.1. Neo
^^^^^^^^^^^

Sagittal AI’s initial offering, Neo, is designed to streamline the software development lifecycle through seamlessly integrating with existing tools. Neo
activates upon work assignments within these tools, gathering scattered contextual information, and directly completing tasks within those same tools while
collaborating with the human team throughout the operation. Neo is designed to support reduced time and cognitive burden. Neo generates sprint status reports by
analyzing Jira tickets and GitHub comments, refactor code from an architecture diagram, resolve P2 bugs using PRDs and Figma documents.

C.14. Scribe Security
~~~~~~~~~~~~~~~~~~~~~

Scribe Security provides an end-to-end software supply chain security SaaS platform that is designed to secure code throughout its life cycle. Scribe Hub
integrates with enterprise pipelines to provide deep visibility, integrity protection, risk insights, and continuous verification.

Scribe signs and verifies the evidence cryptographically, enhances it with open intelligence sources, and analyzes aspects such as integrity to control risk.

C.14.1. ScribeHub
^^^^^^^^^^^^^^^^^

ScribeHub is a comprehensive software supply chain platform for managing SDLC risk and protecting software factories and products from development to
deployment. ScribeHub has automated SDLC security practices (signing, attestations, risk management, prevention, mitigation, and trust) into the DevOps
toolchains in order to support secure-by-design products and reduce security and liability risks. SLDC data is collected by two Scribe tools: Valint, a command
line interface tool for generating, signing, and verification, and Platforms, a tool for generating security posture and security reports evidence, and
verifying evidence and in an agent-less manner.

C.14.2. Heyman
^^^^^^^^^^^^^^

Heyman by Scribe Security is an AI ASPM agent that acts as a virtual AppSec and DevSecOps co-pilot deliver deep, contextual insights from across the software
supply chain that go beyond basic scan aggregation. Integrated with Scribe’s continuous assurance platform, it prioritizes vulnerabilities based on real impact,
automates remediation workflows, and helps teams catch issues early. Heyman supports natural language interaction and seamless integration into developer tools.
