Functional Demonstration Results
=================================


This section describes the functional demonstration results for each of the example implementations. The demonstration results have the notation below. 

Demo ID Notation is as follows:

Example: E1.A-1.1

- E1 = Example Implementation 1

- A-1.1 = Scenario A-1, Demonstration Step 1

Example: E2.D-2.3

- E2 = Example Implementation 2

- D-2.3 = Scenario D-2, Demonstration Step 3

Example Implementation 1 (E1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes the functional demonstration results for the example implementation 1. 

.. _e1-plan-results:

E1 Plan Phase
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.A-1.1 <scenario-a-1>`
     - Users have access to the collaboration tools, project plan, workflows, and assigned tasks.
     - Users were able to access various project tools.
     - | Implemented: User has access to Microsoft Azure DevOps (AzDO) Boards and Work Items for ticketing capabilities, Delivery Plans for requirements, and Sprints/Backlogs for project management.
       |
       | Note: Microsoft AzDO Delivery Plans is a solution for requirements and product management. Delivery Plans was not implemented in this build.
   * - :ref:`E1.A-1.2 <scenario-a-1>`
     - Users are granted access to specific role-based functions which allow required actions and responsibilities to be assumed and executed.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.A-2.1 <scenario-a-2>`
     - Requirements are created and documented in the system.
     - Functional and security requirements input into Microsoft AzDO and tracked
     - Implemented: Functional and security requirements are updated in Microsoft AzDO Delivery Plans under the Boards.
   * - :ref:`E1.A-2.2 <scenario-a-2>`
     - Stakeholders receive assignments.
     - Assignments were assigned in Microsoft AzDO Boards
     - Implemented: Users are assigned tasks under Work Items and requirements are assigned to stakeholders in Delivery Plans in Microsoft AzDO Boards.
   * - :ref:`E1.A-3.1 <scenario-a-3>`
     - Design solutions are documented in the Design Management System to track and maintain product materials for the software application.
     - Requirements solutions input into Microsoft AzDO and tracked
     - Implemented: Requirements are updated in Azure Microsoft AzDO using Delivery Plans.
   * - :ref:`E1.A-3.2 <scenario-a-3>`
     - Tickets are updated based on tasking.
     - Software requirements input into Microsoft AzDO and tracked.
     - | Implemented: Tickets or tasks under Work Items are updated in Microsoft AzDO Boards.

       | Note: Microsoft AzDO Delivery Plans is a solution for requirements and product management. Delivery Plans were not implemented in this build.
   * - :ref:`E1.A-3.3 <scenario-a-3>`
     - | Product requirements and necessary changes to product vision, roadmaps, features, and grow strategy are documented accordingly to track product and
       | component changes.
     - Microsoft AzDO Boards were leveraged to create, assign, and resolve tasks.
     - | Implemented: Product requirements are updated in Microsoft AzDO Boards.

       | Note: Microsoft AzDO Delivery Plans is a solution for requirements and product management. Delivery Plans were not implemented in this build.
   * - :ref:`E1.A-4.1 <scenario-a-4>`
     - High level and technical issues are documented.
     - Issues were documented in Microsoft AzDO Boards.
     - Implemented: Issues were logged under Work Items in Microsoft AzDO Boards.
   * - :ref:`E1.A-4.2 <scenario-a-4>`
     - All issues are assigned to the appropriate team member.
     - Microsoft AzDO Boards was leveraged to assign issues to team members.
     - Implemented: Issues were assigned to a developer and logged under Work Items in Microsoft AzDO Boards.
   * - :ref:`E1.A-5.1 <scenario-a-5>`
     - Risks are identified and documented.
     - | Microsoft Defender for Cloud (MDC) is integrated with Microsoft AzDO to identify and track risks.

       | Black Duck Software Risk Manager (SRM) provided risk assessments.

       | Endor Labs Reachability-Based SCA, Endor Code, Container Scanning, Patches, and AI Code Security Review are all used for risk management.

     - | Implemented: Microsoft MDC and GitHub Advanced Security for Microsoft AzDO received risks associated with the software application from Microsoft AzDO.

       | Note: Microsoft MDC includes components, such as Cloud Ops Security, Cloud Security Posture Management (CSPM), Cloud Workload Protection (CWPP).

       | Implemented: Black Duck Software Risk Manager (SRM) identifies and correlates software findings from Black Duck and third-party tools.

       | Implemented: Endor Labs Reachability-Based SCA, Endor Code, Container Scanning, Patches, and AI Code Security Review all assist with identifying risks and providing remediation suggestions via the Endor Labs Platform. Endor Labs Reachability-Based SCA, Endor Code, Container Scanning, Patches, and AI Code Security Review identify risks and provide details of the risk with remediation suggestions via Endor Labs web front end.
   * - :ref:`E1.A-5.2 <scenario-a-5>`
     - Tickets are created and updated based on new risks. Mitigations and solutions are documented in tickets as risks are resolved.
     - | Microsoft AzDO Work Items are created as tickets.

       | Black Duck Software Risk Manager (SRM) prioritized risks that were identified.

     - | Implemented: Specific risks that need to be resolved were updated in Microsoft AzDO Work items and assigned to a stakeholder to resolve.

       | Implemented: Black Duck SRM generated Microsoft AzDO work items using issue templates.
   * - :ref:`E1.A-6.1 <scenario-a-6>`
     - | Results of cyber intelligence and other security feeds were reviewed and documented. Tickets are created and updated to track and resolve issues related
       | to threats.
     - | Microsoft MDC provided automated assignment of known threats to vulnerable system components.

       | Endor Labs Vulnerability Database provided known vulnerabilities and associated links to existing security metadata sources.

     - | Implemented: Microsoft MDC provides results of issues to cyber intelligence and other security feeds related to the software application.

       | Implemented: Endor Labs Vulnerability Database provides a searchable list of known vulnerabilities and associated security metadata sources such as CVE, NVD, and others.
   * - :ref:`E1.A-6.2 <scenario-a-6>`
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.A-6.3 <scenario-a-6>`
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.A-7.1 <scenario-a-7>`
     - Configurations are created and updated.
     - Microsoft AzDO was leveraged to create specific CI/CD pipelines for various configurations.
     - Implemented: Microsoft AzDO was integrated with Microsoft Azure Dev Center and Managed DevOps Pool to configure CI/CD environments.
   * - :ref:`E1.A-7.2 <scenario-a-7>`
     - | Tickets are created and updated as configurations change. Both Design and Requirements Management Systems are updated to track con-figuration changes
       | over time.
     - Microsoft AzDO Boards was leveraged to perform updates to tickets and requirements.
     - Implemented: Tickets or tasks under Work Items are updated and requirements are updated in Delivery Plans in Microsoft AzDO Boards.
   * - :ref:`E1.A-8.1 <scenario-a-8>`
     - Policies are defined and implemented in certificate, credential and secret management systems.
     - | User IDs created in Entra ID and roles assigned. Secrets are managed within Microsoft Azure Key Vault (AKV) is used for secrets management.

       | DigiCert Software Trust Manager is also leveraged for secrets and certificates.

       | CyberArk Privilege Cloud and

       | CyberArk Secrets Hub was used for management.

     - | Implemented: Entra ID was leveraged to create users and assign roles and policies to the users. Specific Microsoft AzDO permissions related to users were configured within Microsoft AzDO to integrate with Entra ID. Microsoft AzDO also managed security policies related to specific functions. Microsoft AKV was leveraged for secrets lifecycle management.

       | Implemented: DigiCert Software Trust Manager was used to manage secrets such as hash’s, public/private keys, and certificates. It was integrated with Microsoft AzDO so that artifacts and SBOMs can be signed.

       | Implemented: CyberArk Secrets Hub was integrated with Microsoft AKV to monitor secrets to provide visibility and status. Privilege Cloud was leveraged to create secrets, which then can be synchronized with AKV to enable secrets management such as rotation & policy compliance.
   * - :ref:`E1.A-8.2 <scenario-a-8>`
     - Certificates, credentials, and secrets are scanned or tested to verify access and policy configurations.
     - | Users created in Entra ID were tested for their permissions.

       | DigiCert Software Trust Manager used to store secrets

       | CyberArk Privilege Cloud and CyberArk Secrets Hub were used for management.

     - | Implemented: Specific users were tested for access and permissions within Microsoft AzDO. When secrets are used, that information was stored in Azure Container registries under the specific pipeline repository.

       | Implemented: Secrets are securely stored in DigiCert Software Trust Manager and logs can be viewed in the logs sections. Information about keypairs and certificates can also be viewed in those sections of the Trust Manager.

       | Implemented: CyberArk Secrets Hub was synchronized with Microsoft AKV so all secrets in AKV was monitored.
   * - :ref:`E1.A-8.3 <scenario-a-8>`
     - | Certificates, credentials, and secrets are verified as safe to use and are rotated, revoked, or reissues in the event of disclosure or potential vulnerability.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.A-9.1 <scenario-a-9>`
     - CI/CD Pipelines are created, updated, and maintained successfully so automated actions can be performed as required.
     - CI/CD pipelines were created in AzDO to automate various functions.
     - | Implemented: Initial CI/CD pipelines were designed and built to automate the creation of future pipelines for the various phases of the DevSecOps lifecycle.
   * - :ref:`E1.A-9.2 <scenario-a-9>`
     - Configurations, IaC, and source code are obtained by CI/CD Pipelines and are used as part of the build process.
     - Configurations, IaC, and source code were obtained by CI/CD Pipeline.
     - Implemented: Once the CI/CP pipeline was built, we pulled in Configurations, IaC, and source code. Bicep, a domain-specific language from Microsoft, was used to deploy Azure resources for IaC.
   * - :ref:`E1.A-9.3 <scenario-a-9>`
     - Requirements verified and logged by CI/CD Pipelines.
     - CI/CD pipeline configuration is validated.
     - Implemented: CI/CD pipeline is validated against AzDO Delivery Plans.
   * - :ref:`E1.A-10.1 <scenario-a-10>`
     - User access to systems (e.g., Ticketing and Design Management System) is allowed or denied based on ZT policies
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict the user access.
   * - :ref:`E1.A-10.2 <scenario-a-10>`
     - Requirement and design documents are protected and stored. Only authorized personnel can access and distribute them.
     - Microsoft AzDO Leveraged.
     - Implemented: Microsoft AzDO Area Path RBAC was leveraged for the protection of access to user stories, requirements, and design specifications.
   * - :ref:`E1.A-10.3 <scenario-a-10>`
     - Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices, including rotation and short expiration times.
     - Microsoft Entra ID provided token-based authentication via managed identities and workload identity federation.
     - Partially Implemented: Machine/workload identities were implemented to provide machine or service-level authentication using short-lived tokens. Certificate-based authentication and lifecycle management controls will be included in a future Example Implementation.
   * - :ref:`E1.A-11.1 <scenario-a-11>`
     - New work items, tickets, or issues are generated.
     - Sagittal Neo provided analysis of requirements captured in Microsoft AzDO Boards and created new work items.
     - Implemented: Sagittal Neo provides automated analysis of existing context in Microsoft Azure Work Items, source code, and pull requests and generates new work items to track status of requirements.
   * - :ref:`E1.A-11.2 <scenario-a-11>`
     - Existing work items, tickets, or issues are assigned to epics or user stories.
     - Sagittal Neo provided analysis and curation of existing work items in Microsoft AzDO Boards and assigns work to users accordingly.
     - Implemented: Sagittal Neo provides automated analysis of existing context in Microsoft AzDO Boards and created or assigned work items to users.
   * - :ref:`E1.A-11.3 <scenario-a-11>`
     - Duplicate work items, tickets, or issues are marked as closed or removed.
     - Sagittal Neo provided automated closing of duplicate or deprecated work items.
     - Implemented: Sagittal Neo provides automated closing of work items that were deemed closed, duplicated, or deprecated.
   * - :ref:`E1.A-11.4 <scenario-a-11>`
     - Standards or framework compliance requirements are documented for project, requirements, or risk management systems.
     - | GitHub CoPilot provided analysis of standards and frameworks provided as context.

       | Sagittal Neo provided analysis of standards and frameworks provided as context.

     - | Implemented: GitHub CoPilot provides generated suggestions and recommendations on how to resolve discovered findings when analyzing project, requirements, or risk managements system contexts.

       | Implemented: Sagittal Neo provides generated content based on security compliance requirements provided by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.A-11.5 <scenario-a-11>`
     - Summaries are documented in project or requirements management system.
     - | GitHub CoPilot provided summarization of project and task requirements.

       | Sagittal Neo and Semantic Linter provided summarization of project and task requirements in work items.

     - | Implemented: GitHub CoPilot provides generated summaries and documentation based on project and requirements provided as context.

       | Implemented: Sagittal Neo and Semantic Linter provides generated documentation and requirements based on context included in work items.
   * - :ref:`E1.A-11.6 <scenario-a-11>`
     - Required resources are identified, documented for project or design management systems.
     - | GitHub CoPilot identified specific resources (e.g., source code, functions, software dependencies) required based on user-provided context.

       | Sagittal Neo and Semantic Linter identified specific resources (e.g., source code, functions, software dependencies) required by project-specific work items.

     - | Implemented: GitHub CoPilot provides specific source code changes, function, and software dependencies based on project and requirements provided as context.

       | Implemented: Sagittal Neo and Semantic Linter provides specific source code changes, functions, or software dependencies associated with project-specific work items, source code, or pull requests.
   * - :ref:`E1.A-11.7 <scenario-a-11>`
     - Modifications are generated and saved for future use.
     - | GitHub CoPilot provided analysis of requirements captured as user-provided context and saved generated modifications as source code commits or branches.

       | Sagittal Neo provided analysis of requirements captured in Microsoft AzDO Boards, Pull Requests, and source code commits and created new work items.

     - | Implemented: GitHub CoPilot provides automated analysis of existing source code, documentation, and user-provided context to generate changes to source code in the form of new commits or branches.

       | Implemented: Sagittal Neo provides automated analysis of existing context in Microsoft AzDO Boards such as work items, source code, and pull requests and generates new work items to track status of requirements.
   * - :ref:`E1.A-11.8 <scenario-a-11>`
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - Sagittal Neo provided analysis of risks and vulnerabilities provided as context from Black Duck Software Risk Manager issue templates.
     - | Implemented: Sagittal Neo provides generated content based on associated security requirements included work items created by the Black Duck Software Risk Manager issue templates.

       | Note: Black Duck Software Risk Manager has a Triage Assistant built into the platform which identifies remediation steps taken and recommends an update to the risk based upon prior actions. Triage Assistant was not implemented as part of this demonstration.
   * - :ref:`E1.A-11.9 <scenario-a-11>`
     - Users, service accounts, or other principals are identified in credential or secrets management system.
     - Sagittal Neo provided checklist items and work items that identify the existence of detected secrets.
     - | Implemented: Sagittal Neo provides generated content based on detected secrets documented in work items either manually assigned or generated by the Black Duck Software Risk Manager issue templates.

.. _e1-develop-results:

E1 Develop Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.B-1.1 <scenario-b-1>`
     - Source code, unit tests, and automation scripts are created.
     - | AzDO was used to create and manage software application development. Visual Studio code (VS Code) was leveraged for code development.

       | Microsoft GitHub Copilot analyzed code and helped update unit tests.

       | Endor Labs endorctl (CLI tool) was leveraged to run code.

     - | Implemented: Leveraged AzDO to provide SCM capabilities, BICEP to automate the development of IaC. Microsoft VS Code was used for code development in this phase.

       | Implemented (AI Enhancement): Microsoft GitHub Copilot is integrated with VS Code, in this experiment, to analyze code. User input information into the prompt. Copilot ingested the information and responded with next steps. The user acknowledged and instructed Copilot to perform the next steps.

       | Implemented: endorctl (CLI tool) was leveraged to test code. Various tools (Reachability-Based SCA, Endor Code, Container Scanning, Patches, and AI Code Security Review) were used to run against the code via endorctl.

       | Note: Endor Labs provide risk details, impact, and mitigation (with references) to each finding.
   * - :ref:`E1.B-1.2 <scenario-b-1>`
     - Artifacts are retrieved and managed via a repository.
     - Repositories were created in AzDO to manage artifacts.
     - | Implemented: In this phase, pipelines were created along with associated repositories to store and manage artifacts using Azure Artifacts. Azure Container Registry (ACR) was used to manage container images.
   * - :ref:`E1.B-1.3 <scenario-b-1>`
     - Code is built and unit tests are run.
     - | Microsoft AzDO was used to create source code changes.

       | Microsoft Visual Studio Code provided IDE functions necessary to create source code changes.

     - | Implemented: Microsoft AzDO was utilized to execute source code changes as part of the build and publish test results. Microsoft Visual Studio Code was utilized to execute source code changes as part of the build and publish test results.
   * - :ref:`E1.B-2.1 <scenario-b-2>`
     - Any vulnerabilities are found, and logs are provided.
     - | Microsoft AzDO SAST capabilities were used.

       | Black Duck Polaris Platform was used for SAST.

       | Endor Labs Endor Code was used to perform SAST.

     - | Implemented: During pipeline development, Microsoft GitHub Advanced Security for Azure DevOps (GHAzDO) was configured, executed against software, and identified vulnerabilities.

       | Implemented: Black Duck Polaris Platform was integrated with AzDO, into the CI/CD pipeline to analyze source code with its Coverity SAST capability. Vulnerabilities were identified and assessed for risk using policies within a main code branch and in feature branches.

       | Implemented: Endor Labs Endor Code was used to perform SAST. Vulnerabilities were logged. Note: Endor Labs provide risk details, impact, and mitigation (with references) for each finding.
   * - :ref:`E1.B-2.2 <scenario-b-2>`
     - Security issues and style problems are found via the linting tool. Logs are provided to the developer.
     - Microsoft AzDO Linting capabilities were used.
     - | Implemented: the development of the CI/CD pipeline executed the security tools with no errors. Logs were provided in AzDO.

       | Note: PSRule can be incorporated to validate Bicep templates for security and compliance issues.

       | Note: The process of using Microsoft GitHub Copilot to analyze vulnerabilities identified by a lint tool is the same as the process for SAST vulnerabilities.
   * - :ref:`E1.B-2.3 <scenario-b-2>`
     - SCA tool runs, vulnerabilities are detected, and logs are provided.
     - | Microsoft AzDO SCA capabilities were used.

       | Black Duck Polaris Platform SCA was used.

       | Endor Labs Reachability-Based SCA was used.

     - | Implemented: The development of the CI/CD pipeline executed the SCA security tools (GHAzDO) with no errors. Logs were provided in AzDO to Microsoft MDC: Cloud Workload Protection (CWPP) – Containers, DevOps Security.

       | Implemented: Black Duck Polaris Platform SCA capabilities were integrated with AzDO to analyze third-party libraries for vulnerabilities. Package manager analysis shows both transitive and declared components, while signature analysis identifies code added to the project outside of a package manager. A complete dependency tree is provided. Remediation guidance includes a short-term fix option within the current major version of a library and longer-term suggestions where additional coding might be required. All findings are logged and can be triaged.

       | Implemented: Endor Labs Reachability-Based SCA was executed and findings logged. Where applicable, specific risk details and remediation are provided.
   * - :ref:`E1.B-2.4 <scenario-b-2>`
     - Credentials, Keys, and other sensitive information are detected. Results are provided to developers.
     - | Microsoft AzDO GHAzDO was leveraged to detect sensitive information.

       | Black Duck Polaris Platform was leveraged to detect sensitive information.

       | Endor Labs Endor Code was leveraged to scan for exposed secrets.

     - | Implemented: The development of the CI/CD pipeline executed scans using GHAzDO to detect sensitive information. Logs were provided in AzDO of findings.

       | Implemented: Black Duck Polaris Platform scanned for exposed secrets. Findings are logged and a ticket was created through the integration of SRM to Microsoft AzDO.

       | Implemented: Endor Labs Endor Code, which contains both SAST and Secret Scanning capabilities, was leveraged to scan for exposed secrets. Exposed secrets were logged. Risk details and remediation were provided where applicable.
   * - :ref:`E1.B-3.1 <scenario-b-3>`
     - IaC scripts are created.
     - Microsoft Bicep was used to create IaC.
     - | Implemented: scripts were developed in Bicep to create IaC and leverage it for subsequent phases. This was created in a separate pipeline. CI/CD pipelines are then created to leverage this and outputs stored in Microsoft AzDO Repos.
   * - :ref:`E1.B-3.2 <scenario-b-3>`
     - IaC code problems are found and logs provided.
     - | Microsoft GHAzDO was leveraged to scan IaC vulnerabilities.

       | Black Duck Polaris was leveraged to scan IaC vulnerabilities.

       | Endor Labs Endor Code was leveraged to scan for IaC vulnerabilities

     - | Implemented: Microsoft GHAzDO ran several IaC scanner tools (e.g., iacfilescanner, checkov, and template-analyzer) and identified vulnerabilities. This was executed in a separate pipeline.

       | Note: PSRule can be incorporated to validate Bicep templates for security and compliance issues.

       | Implemented: Black Duck Polaris scanned the Kubernetes setup and identified vulnerabilities.

       | Implemented: Endor Labs Endor Code was leveraged to scan for IaC vulnerabilities. Identified vulnerabilities were logged. Risk details and remediation were provided where applicable.
   * - :ref:`E1.B-4.1 <scenario-b-4>`
     - Changes are reviewed by approved developers prior to merging.
     - Microsoft AzDO was leveraged to assign users to issues.
     - Implemented: Execution of pipelines results in findings. AzDO Work items are created to track issues and approved developers review them before merging.
   * - :ref:`E1.B-4.2 <scenario-b-4>`
     - Code is created by developers and committed to source code repositories.
     - Microsoft AzDO provided storage and management of source code committed by developers.
     - | Implemented: Microsoft AzDO provides individual source code repositories where developers can commit source code changes and manage the state of source code. Note: This demonstration was added in Example Implementation 2 but was still verified for Example Implementation 1.
   * - :ref:`E1.B-4.3 <scenario-b-4>`
     - Code is scanned and is not committed if errors are found.
     - | AzDO pipelines executed scans.

       | Black Duck Polaris was leveraged to perform SAST and SCA scans.

       | Endor Labs Endor Code and Reachability-Based SCA tools were used to perform scans.

     - | Implemented: AzDO GHAzDO identified vulnerabilities from pipeline scans. Microsoft GitHub Copilot performed Linting based on user input. Errors are logged in Microsoft MDC components: Cloud Workload Protection (CWPP) – Containers, DevOps Security for SCA.

       | Implemented: Black Duck Polaris’s SAST, SCA, and secret scanning capabilities identified vulnerabilities. Code scanning was performed on a main branch for merged code, in addition to scanning feature branches prior to merging code. Results are provided within the Polaris UI, SCM PR comments, and within developer tools such as VS Code.

       | Implemented: Endor Labs Endor Code and Reachability-Based SCA tools were used to perform scans.
   * - :ref:`E1.B-4.4 <scenario-b-4>`
     - Code that has not been approved cannot be merged into main.
     - Microsoft AzDO project settings-Repositories settings configured for repository security.
     - | Implemented: AzDO Project Settings for repositories, including specific policies were defined by the administrator for code commits and other related functions.
   * - :ref:`E1.B-5.1 <scenario-b-5>`
     - Credentials are stored and managed securely.
     - Microsoft AzDO leveraged Microsoft AKV to manage sensitive information and Entra ID to manage users.
     - | Implemented: The development CI/CD pipeline was set up to leverage Microsoft AKV to manage sensitive information securely. Entra ID was leveraged to create users and assign roles and policies to the users. Specific AzDO permissions related to users were configured in order to integrate with Entra ID.
   * - :ref:`E1.B-5.2 <scenario-b-5>`
     - Keys and other secrets are stored and managed securely.
     - | Microsoft AzDO leveraged Microsoft AKV to manage sensitive information.

       | DigiCert Software Trust Manager was used to provide and manage secrets.

     - | Implemented: The development CI/CD pipeline was set up to leverage Microsoft AKV to manage sensitive information securely.

       | Implemented: DigiCert Software Trust Manager was used to provide and manage key pairs and certificates as needed throughout the phases.
   * - :ref:`E1.B-5.3 <scenario-b-5>`
     - Certificates are stored and managed (e.g., issuance, rotation, revocation) securely.
     - | Microsoft AzDO leveraged Microsoft AKV to manage sensitive information.

       | Public certificates provided by DigiCert are securely stored by DigiCert Software Trust Manager.

     - | Partially implemented: The development CI/CD pipeline was set up to leverage Microsoft AKV to manage sensitive information securely.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection.
       | The current subscription of AzDO does not have an HSM to store certificates and other secrets. An upgraded subscription of AzDO provides hardware back HSM capabilities.

       | Implemented: Public certificates provided by DigiCert are securely stored by DigiCert Software Trust Manager. Note: For a public trust certificate provided by DigiCert, the key is stored on a shared HSM, which is FIPS compliant. DigiCert can also provide dedicated HSM. For disk based (non-public) keys, a non-FIPS compliant software based HSW was used by DigiCert. For this experiment, both public and non-public certs were used.
   * - :ref:`E1.B-6.1 <scenario-b-6>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.B-6.2 <scenario-b-6>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.B-6.3 <scenario-b-6>`
     - Logs of firmware updates or changes are captured
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.B-7.1 <scenario-b-7>`
     - Software components are digitally signed, and secrets are stored and protected by HSM.
     - | Microsoft AKV is leveraged to manage the signing of software components.

       | Signed certificates by DigiCert are securely stored by DigiCert Software Trust Manager.

     - | Partially implemented: Microsoft AKV is leveraged to manage secrets used to sign software components and the results can be found in Azure Container registries under the specific repository of the pipeline used.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection. The current subscription of AzDO does not have an HSM to store certificates and other secrets.

       | Implemented: Signed public certificates provided by DigiCert are securely stored by DigiCert Software Trust Manager. Note: For a public trust certificate provided by DigiCert, the key is stored on a shared HSM, which is FIPS compliant.
   * - :ref:`E1.B-7.2 <scenario-b-7>`
     - Signed software components are authentic and not tampered with.
     - | Azure Container registries store information as proof.

       | DigiCert Software Trust Manager certificates and key pairs are protected.

     - | Implemented: the results of the manifest in Azure Container registries under the specific repository of the pipeline is proof that the software component has not been tampered with.

       | Implemented: Signed public certificates or key pairs provided by DigiCert are securely managed and stored by DigiCert Software Trust Manager and cannot be tampered with.
   * - :ref:`E1.B-7.3 <scenario-b-7>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - | Logging provided in Azure Container registries. No alerts sent.

       | DigiCert Software Trust Manager alerts via email by default.

     - | Implemented: Details of the results of the manifest are provided in Azure Container registries under the specific repository of the pipeline. This provides integrity verification. Microsoft AzDO generates and retains audit logs and can issue notifications; Microsoft Sentinel can also be used for alerting and notification workflows.

       | Implemented: DigiCert Software Trust Manager can send emails as a way of notification. Integration with other tools for alerts is available.
   * - :ref:`E1.B-8.1 <scenario-b-8>`
     - Certificates and private keys are stored and managed securely in the Certificate Management System.
     - | Microsoft AKV was used to store certificates.

       | DigiCert Software Trust Manager managed certificates.

     - | Implemented: certificates are stored in Microsoft AKV.

       | Implemented: Signed public certificates provided by DigiCert are securely managed and stored by DigiCert Software Trust Manager and cannot be tampered with. It is encrypted at rest.
   * - :ref:`E1.B-8.2 <scenario-b-8>`
     - Secrets and credentials are securely managed and stored in Secrets Management System.
     - | Microsoft AKV was used to store secrets and credentials.

       | Secrets are managed by DigiCert Software Trust Manager.

     - | Implemented: secrets and credentials are stored in Microsoft AKV.

       | Implemented: DigiCert Software Trust Manager manages secrets created by DigiCert.
   * - :ref:`E1.B-9.1 <scenario-b-9>`
     - Scripts to automate the CI/CD pipelines and build its environments are stored in SCM.
     - Microsoft AzDO stored the scripts
     - Implemented: Microsoft AzDO repositories were leveraged to store configuration information.
   * - :ref:`E1.B-10.1 <scenario-b-10>`
     - Only authorized users can access and perform actions on source code management systems.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict the user.
   * - :ref:`E1.B-10.2 <scenario-b-10>`
     - Only authorized endpoints can access source control systems and development systems.
     - Microsoft Entra Conditional Access leveraged.
     - | Implemented – Microsoft Entra Conditional Access policy for the cloud app “Azure DevOps” can be created and enforce user access. Azure Policy can also be
       | used to constrain what can be deployed. Microsoft Intune and Defender for Endpoint can be integrated to provide device posture capabilities.
   * - :ref:`E1.B-10.3 <scenario-b-10>`
     - Authorized users can make changes to restricted branches.
     - Azure policies were applied to users.
     - | Implemented: Policies were implemented in Azure Entra ID and AzDO (within AzDO Teams and Permissions settings) to restrict certain users from accessing specific AzDO capabilities.
   * - :ref:`E1.B-10.4 <scenario-b-10>`
     - | Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices,
       | including rotation and short expiration times.
     - Microsoft Entra ID provided token-based authentication via managed identities and workload identity federation.
     - Partially Implemented: Machine/workload identities were implemented to provide machine or service-level authentication using short-lived tokens. Certificate-based authen-tication and lifecycle management controls will be included in a future Example Implementation.
   * - :ref:`E1.B-10.5 <scenario-b-10>`
     - Only pipeline runs satisfying the applicable ZT policy conditions are permitted to advance.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.B-11.1 <scenario-b-11>`
     - Source code and configuration files are generated and changes, explanations, and commits are captured.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.B-11.2 <scenario-b-11>`
     - Source code and configuration files are updated with generated changes and documented explanations.
     - | GitHub CoPilot generated source code, configuration, and documentation changes.

       | Sagittal Neo generated source code, configuration, and documentation changes for projects hosted in Microsoft Azure DevOps.

     - | Implemented: GitHub CoPilot generated content based on existing source code, configuration files, and project documentation accessible through Visual Studio Code.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Microsoft AzDO source code repositories.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.3 <scenario-b-11>`
     - Code and configurations are brought into compliance with specified standards.
     - | GitHub CoPilot provided code and configuration changes based on user-provided security and compliance requirements.

       | Sagittal Neo provided code and configuration changes based on security and other compliance requirements.

     - | Implemented: GitHub CoPilot provides code and configuration changes based on user-provided security context.

       | Implemented: Sagittal Neo provides code and configuration changes based on security reports generated by Black Duck Software Risk Manager issue templates.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.4 <scenario-b-11>`
     - Vulnerabilities are remediated through refactored code and committed to SCM.
     - | GitHub CoPilot provided code and configuration changes based on user-provided security and compliance requirements.

       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.

       | Black Duck AI Insights generated code and configuration suggestions based on identified security and compliance findings.

     - | Implemented: GitHub CoPilot provides code and configuration changes based on user-provided security context.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings generated by Black Duck Software Risk Manager issue templates.

       | Implemented: Black Duck AI Insights provides generated code suggestions and potential remediations based on linked security and compliance findings collected by Black Duck Polaris Platform.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11-5 <scenario-b-11>`
     - Dependency lists are optimized to remove or replace vulnerable libraries and updates are reflected in SCM or artifact repositories.
     - | GitHub CoPilot provided software dependency changes based on security and other compliance requirements.

       | Sagittal Neo provided software dependency changes based on security and other compliance requirements.

       | Black Duck AI Insights generated software dependency changes based on identified security and compliance findings.

     - | Implemented: GitHub CoPilot provides code and configuration changes based on user-provided security findings and scanning reports as context.

       | Implemented: Sagittal Neo provides software dependency changes based on detected security findings or provided reports that require remediation.

       | Implemented: Black Duck AI Insights provides generated software dependency suggestions based on detected vulnerabilities collected by Black Duck Polaris Platform.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.6 <scenario-b-11>`
     - Source code and source control artifacts are updated with generated commits, branches, and pull requests.
     - | GitHub CoPilot generated source code, configuration, and documentation changes.

       | Sagittal Neo generated source code, configuration, and documentation changes for projects hosted in Microsoft Azure DevOps.

     - | Implemented: GitHub CoPilot generated content based on existing source code, configuration files, and project documentation accessible through Visual Studio Code.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Microsoft AzDO source code repositories.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.7 <scenario-b-11>`
     - Compliance requirements are provided and includes steps to replace non-compliant dependencies with acceptable alternatives.
     - | GitHub CoPilot provided software dependency changes based on security and other compliance requirements.

       | Sagittal Neo provided software dependency changes based on security and other compliance requirements.

       | Black Duck AI Insights generated software dependency changes based on identified security and compliance findings.

     - | Implemented: GitHub CoPilot provides code and configuration changes based on user-provided licensing and security reports.

       | Implemented: Sagittal Neo recommends changing dependencies based on licensing and security reports that provide findings and proposed remediations.

       | Implemented: Black Duck AI Insights provides generated software dependency suggestions based on detected vulnerabilities collected by Black Duck Polaris Platform.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.8 <scenario-b-11>`
     - | Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or credentials.
     - | GitHub CoPilot provided code and configuration changes based on user-provided security and compliance requirements.

       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.

       | Black Duck AI Insights generated code and configuration suggestions based on identified security and compliance findings.

     - | Implemented: GitHub CoPilot provides code and configuration changes based on user-provided security findings and scanning reports as context.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings generated by Black Duck Software Risk Manager issue templates.

       | Implemented: Black Duck AI Insights provides generated code suggestions and potential remediations based on linked security and compliance findings collected by Black Duck Polaris Platform.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.B-11.9 <scenario-b-11>`
     - Plans are generated and provide methods to mitigate or remediate vulnerabilities found in artifacts.
     - Sagittal Neo generated source code, configuration, and documentation changes for projects hosted in Microsoft Azure DevOps.
     - | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Microsoft AzDO source code repositories.

.. _e1-build-results:

E1 Build Phase
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.C-1.1 <scenario-c-1>`
     - CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed.
     - CI/CD Pipelines were provisioned
     - | Implemented: The Build CI/CD pipeline is provisioned, which includes the provision of IaC. Note that SCM and configuration management capabilities are included in AzDO, for example in AzDO Repos.
   * - :ref:`E1.C-1.2 <scenario-c-1>`
     - Configurations, IaC, and source code are obtained by CI/CD pipelines and are used as part of the build process.
     - Pipeline leveraged IaC and pulled in Juice Shop source code.
     - | Implemented: Results of the pipeline output showed that IaC was working, and source code was pulled into the pipeline to be executed. Note, this pipeline is leveraging IaC, which was built in a separate pipeline.
   * - :ref:`E1.C-1.3 <scenario-c-1>`
     - CI/CD Pipelines run all build process components, and each component generates output for tracking status and logging de-tailed information.
     - Build CI/CD pipeline run was completed successfully.
     - Implemented: The CI/CD pipeline was initiated and completed. Summary and raw logs provided.
   * - :ref:`E1.C-1.4 <scenario-c-1>`
     - | Output that was logged by the CI/CD Pipelines are returned to SCM and Configuration Management Systems to track status and detailed information about the build process.
     - Outputs are logged by the CI/CD pipeline in AzDO.
     - Implemented: All outputs are logged after the pipeline is executed under the specific pipeline and stored in the corresponding Repos.
   * - :ref:`E1.C-1.5 <scenario-c-1>`
     - Components and artifacts either deployed, managed, or used by the build process are leveraging approved configurations.
     - Components and artifacts were either deployed or managed using a separate pipeline.
     - Implemented: The CI/CD pipeline leveraged a separate pipeline as approved environment variables.
   * - :ref:`E1.C-1.6 <scenario-c-1>`
     - Components and artifacts that have been updated in the build are added to the configuration management system.
     - New configurations that are accepted are stored in AzDO.
     - Implemented: Once updates are added to the main branch of the CI/CD pipeline, it is stored in the AzDO Repos accordingly.
   * - :ref:`E1.C-2.1 <scenario-c-2>`
     - The build environment is isolated from host systems or other environments and is automated.
     - Build environment was automated via a separate pipeline built with isolated/hermetic environment specifications.
     - | Implemented: A separate pipeline is created to ensure the build environment is created in isolation and can be recreated each time.
   * - :ref:`E1.C-2.2 <scenario-c-2>`
     - The CI/CD pipeline used CLI tools and binaries and accessed libraries within the isolated environment.
     - | CLI tools, binaries and accessed libraries are used in a separate pipeline built with isolated/hermetic environment specifications.

       | Endor Labs endorctl (CLI tool) was leveraged.

     - | Implemented: A separate pipeline has CLI tools and binaries built and isolated from other environments. Azure MDP was leveraged.

       | Implemented: Endor Labs endorctl is integrated into the CI/CD pipeline to interact with various Endor Labs tools.
   * - :ref:`E1.C-2.3 <scenario-c-2>`
     - Artifacts are created and stored in the artifact repository.
     - The Build repository successfully stored and published artifacts.
     - Implemented: Juice shop artifacts were stored in AzDO Artifacts and ACR.
   * - :ref:`E1.C-3.1 <scenario-c-3>`
     - IaC Scanner identifies security vulnerabilities and compliance issues before IaC is executed.
     - | AzDO scanned IaC scripts prior to execution.

       | Black Duck Polaris performed IaC scans.

       | Endor Labs Endor Code scanned for IaC vulnerabilities.

     - | Implemented: Microsoft GHAzDO ran several IaC scanner tools (e.g., iacfilescanner, checkov, and templateanalyzer) and identified vulnerabilities. This was executed in a separate pipeline. PSRule was incorporated to validate Bicep templates for security and compliance issues.

       | Implemented: Black Duck Polaris scanned the Kubernetes clusters and identified vulnerabilities.

       | Implemented: Endor Labs Endor Code scanned for IaC vulnerabilities. Results of vulnerabilities are logged with risk details and remediation information.
   * - :ref:`E1.C-3.2 <scenario-c-3>`
     - Issues are created and resolved, and logs of changes are maintained.
     - | Issues logged in AzDO and updates made to resolve issues.

       | Black Duck Polaris was leveraged.

       | Endor Labs Endor Code used.

     - | Implemented: A separate pipeline ran the tools and logged the issues. Issues are resolved before the IaC is used by other pipelines.

       | Implemented: Black Duck Polaris logged the identified vulnerabilities, which can be configured to be triaged and resolved.

       | Implemented: Endor Code logs are leveraged to resolve issues.
   * - :ref:`E1.C-3.3 <scenario-c-3>`
     - Build environment is provisioned and managed based on scanned IaC artifacts to ensure consistency.
     - Build environment is provision via a separate pipeline.
     - Implemented: A separate pipeline ensures consistency of the Build environment.
   * - :ref:`E1.C-4.1 <scenario-c-4>`
     - Vulnerabilities, compliance issues, and security risks from software libraries are identified.
     - | Vulnerabilities are identified by the SCA and logged.

       | Black Duck Polaris was leveraged for SAST and SCA scans.

       | Vulnerabilities identified by Endor Labs Reachability-Based SCA and Endor Code.

     - | Implemented: Microsoft AzDO was used to identify dependency vulnerabilities.

       | Implemented: Black Duck Polaris’s SAST and SCA capabilities identified vulnerabilities in both 1\ :sup:`st` party and 3\ :sup:`rd` party code and CVEs published in the NVD along with Black Duck Security Advisories (BDSAs). Policies were evaluated and risk scores calculated. Contextual remediation guidance was provided. Risk reports based on standardized taxonomies were generated. Results were then reported back to Microsoft AzDO for remediation.

       | Implemented: Endor Labs Reachability-Based SCA and Endor Code performed SCA and SAST scans. Vulnerabilities were identified, categorized, and logged. Remediation solutions were provided if available.
   * - :ref:`E1.C-4.2 <scenario-c-4>`
     - Software library artifacts used as part of the build are stored in the artifact repository.
     - Repository stored the artifacts and published it for user download.
     - Implemented: AzDO Repos successfully stored the artifacts.
   * - :ref:`E1.C-5.1 <scenario-c-5>`
     - Unit tests are pulled from SCM and run successfully against known functional criteria.
     - CI/CD pipeline is configured to run all unit tests for the app.
     - Implemented: The CI/CD pipeline successfully ran the unit tests. Microsoft GitHub Copilot was leveraged to run specific unit tests.
   * - :ref:`E1.C-5.2 <scenario-c-5>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results including issues (e.g., defects) in the ticketing system.
     - Outputs are recorded by the pipeline.
     - Implemented: test outputs are logged and AzDO provides raw logs for detailed information.
   * - :ref:`E1.C-6.1 <scenario-c-6>`
     - | CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed for security SAST, SCA, IaC Scanner, Secrets Scanner, and linting tools.
     - | Once pipeline was executed, security tools performed its functions.

       | Black Duck Polaris was leveraged for SAST and SCA scans.

       | Endor Labs Reachability-Based SCA and Endor Code were used.

     - | Implemented: The CI/CD pipeline executed the security tools (e.g., GHAzDO) with no errors.

       | Implemented: The Black Duck Polaris platform was integrated into the CI/CD pipeline, which executed Black Duck Polaris’s SAST and SCA capabilities.

       | Implemented: The Endor Labs tools were integrated into the CI/CD pipeline to run SAST and SCA scans using endorctl.
   * - :ref:`E1.C-6.2 <scenario-c-6>`
     - Code is created and each security tool generates results.
     - | Results are created in Azure AzDO.

       | Black Duck SRM recorded results.

       | Endor Labs provided results of scans.

       | Sagittal Neo was assigned to resolve a SAST issue

     - | Implemented: Results are provided in the summary page of the pipeline and vulnerabilities for the tools are provided in the Advanced Security page under the Repos tab.

       | Implemented: The CI/CD pipeline, which integrated Black Duck Polaris’s SAST and SCA capabilities, initiated the scans. Findings were logged in Black Duck SRM which can be reported back to AzDO for remediation.

       | Implemented: The CI/CD pipeline, which integrated Endor Labs’ SAST and SCA capabilities, provided findings and recommended remediations.

       | Implemented: Neo was assigned to an issue identified by Black Duck SRM from the Polaris SAST scans through an AzDO Work Item. Once the Work Item was created in AzDO, Neo began working of the ticket. Neo created a PR to resolve this issue. Neo provided updates in the Description section and actual development details were provided on the same page of the Work Item. Based on the settings created in AzDO for Repos and pipelines (PR execution and updates), Neo waits for feedback if needed. Neo then committed the updates.

       | Note: Neo can be assigned issues related to linting, SCA, secrets, and SCM. These were not performed as they are similar to the process done above.
   * - :ref:`E1.C-6.3 <scenario-c-6>`
     - Security tools provide outputs of issues via notifications or logs to stakeholders.
     - | Severity levels are applied to each vulnerability found.

       | Black Duck Polaris provided logs.

       | Endor Labs Action Policies & Notifications.

     - | Partially implemented: In this build, no tools were procured to integrate with AzDO for notification purposes. Tools such as Slack or other communication tools can be integrated with AzDO to provide notification capabilities.

       | Partially Implemented: Black Duck Polaris provided logs. SRM was leveraged to create Work Items in AzDO. However, there was no notification sent to stakeholders as explained above.

       | Not Implemented: Endor Labs provides Action Policies to users to help automate notifications, ticket creation, etc. Endor Labs also provides native integrations and webhooks to send notifications or logs to stakeholders.
   * - :ref:`E1.C-7.1 <scenario-c-7>`
     - Sensitive information was securely retrieved during the build process.
     - | AzDO is configured with various services to secure sensitive information.

       | DigiCert Software Trust Manager provided certificates and keys securely.

     - | Implemented: The CI/CD pipeline is configured to retrieve sensitive information securely.

       | Implemented: During the CI/CD pipeline execution, signed public certificates or key pairs are retrieved securely from DigiCert Software Trust Manager.

       | Note: Both certificate and key profiles were created in DigiCert Software Trust Manager for consistent signing of artifacts and other software materials.
   * - :ref:`E1.C-7.2 <scenario-c-7>`
     - Sensitive information is protected by various management systems and HSMs to prevent unauthorized access and disclosure.
     - DigiCert Software Trust Manager was leveraged to manage and protect sensitive information.
     - | Implemented: DigiCert Software Trust Manager securely manages key pairs and certificates. HSM was used for storage. Refer to E1.B-5.3 about details of HSMs.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection. The current subscription of AzDO does not have an HSM to store certificates and other secrets.
   * - :ref:`E1.C-7.3 <scenario-c-7>`
     - The Build phase environment has authorized access to sensitive information with proper credentials and configuration.
     - | AzDO leveraged a credential management system to manage sensitive information.

       | DigiCert Software Trust Manager was integrated with AzDO.

     - | Implemented: The CI/CD pipeline leveraged Microsoft AKV aServiceConnection for credential management.

       | Implemented: DigiCert Software Trust Manager was integrated with AzDO and proper credentials were set up so that certificates and key pairs were securely retrieved from Software Trust Manager.
   * - :ref:`E1.C-7.4 <scenario-c-7>`
     - The HSM is tamper-resistant in maintaining digital assets (e.g., private keys and certificates).
     - DigiCert Software Trust Manager leveraged an HSM for the current build.
     - | Implemented: A FIPS compliant shared HSM for DigiCert was used in this implementation where public certs were used. DigiCert Software Trust Manager also leveraged a self-hosted soft HSM for self-signed certs and key pairs.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection.
       | The current subscription of AzDO does not have an HSM to store certificates and other secrets.


   * - :ref:`E1.C-8.1 <scenario-c-8>`
     - Source code or configuration credentials that are exposed are detected prior to the build.
     - | Exposed credentials were captured in AzDO

       | Black Duck Polaris detected exposed credentials

       | Endor Labs Endor Code detected exposed secrets

       | Neo was assigned to resolve a secrets issue

     - | Implemented: Exposed credentials were identified in AzDO Advanced Security “Secrets” tab.

       | Implemented: Black Duck Polaris performed secret scanning, and findings are reported back to AzDO via SRM in the form of Work Item creation for remediation.

       | Implemented: Endor Labs Endor Code scanned for exposed secrets, which can be viewed under the specific project.

       | Implemented: Neo was assigned to an issue identified by Black Duck SRM from the Polaris scans which detected an exposed secret. Through the integration of Black Duck and AzDO, a Work Item was created by SRM. Once the Work Item was created in AzDO, Neo began working of the ticket. Neo created a PR to resolve this issue. Neo provided updates in the Description section and actual development details were provided on the same page of the Work Item. Based on the settings created in AzDO for Repos and pipelines (PR execution and updates), Neo waits for feedback if needed. Neo then committed the updates.

       | Note: Neo can be assigned issues related to linting, SCA, and SCM. These were not performed as they are similar to the process done above.
   * - :ref:`E1.C-8.2 <scenario-c-8>`
     - Findings are logged by SCA and stakeholders are notified.
     - | Exposed credentials and SCA findings were logged in AzDO Advanced Security.

       | Black Duck Polaris sent logs to Black Duck SRM.

       | Endor Labs logged SCA findings.

     - | Partially Implemented: exposed secrets and SCA findings are logged in the “Secrets” and “Dependencies” tabs of AzDO Advanced Security.

       | Note: Microsoft MDC supports alert notifications and integrates with ticketing systems (for example, ServiceNow). Microsoft AzDO also supports project-level notifications that can be routed to configured email recipients.

       | Partially Implemented: Black Duck Polaris provided logs to SRM which sent it to AzDO as Work Items. However, there was no notification sent to stakeholders as explained above.

       | Partially Implemented: exposed secrets are logged by Endor Labs, but notifications are not set up. In the Endor Labs web interface, exposed secrets can be viewed under the specific project. Notifications can be set up with Action Policies or Webhooks.
   * - :ref:`E1.C-9.1 <scenario-c-9>`
     - Software packages (e.g., artifacts and dependencies) are securely stored and managed in the artifact repository.
     - Azure Artifacts was used.
     - Implemented: Artifacts are stored in the repository (AzDO Artifacts and ACR).
   * - :ref:`E1.C-9.2 <scenario-c-9>`
     - Information is logged by each tool for auditing of the build status.
     - | Logs are recorded in AzDO.

       | Logs recorded in Black Duck and integrated with AzDO.

       | Logs recorded in Endor Labs.

     - | Implemented: Logs are provided in pipeline in the individual jobs.

       | Implemented: Black Duck Polaris scanned vulnerabilities are logged in SRM, which then can submit a Work Item in AzDO.

       | Implemented: all information is logged per project with Endor Labs, which can also be exported.
   * - :ref:`E1.C-10.1 <scenario-c-10>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.C-10.2 <scenario-c-10>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.C-11.1 <scenario-c-11>`
     - Software components are digitally signed and secrets are stored and protected by HSM.
     - | Artifacts are signed in AzDO.

       | An HSM was used by DigiCert Software Trust Manager.

     - | Partially Implemented: Generated containers and packaged artifacts are configured to be digitally signed with a cryptographic hash function.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection.
       | The current subscription of AzDO does not have an HSM to store certificates and other secrets.

       | Implemented: Where DigiCert was used for the demonstration, a FIPS compliant shared HSM was used in this implementation where public certs were used. DigiCert Software Trust Manager also leveraged a self-hosted software HSM for self-signed certs and key pairs.
   * - :ref:`E1.C-11.2 <scenario-c-11>`
     - Signed software components are authentic and not tampered with.
     - Artifacts were signed with cryptographic hash function.
     - Implemented: cryptographic hash function ensured that the artifacts are not tampered with.
   * - :ref:`E1.C-11.3 <scenario-c-11>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - AzDO provided logs.
     - Implemented: Azure Advanced Security provided detailed logs of findings. Alerting capabilities are not available for this demonstration.
   * - :ref:`E1.C-12.1 <scenario-c-12>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - This demonstration has been deferred to a future example implementation.
     - | This demonstration has been deferred to a future example implementation.

       | Note: Microsoft AzDO Marketplace extensions can generate SLSA provenance artifacts (for example, Xygeni Build Attestation; SLSA Provenance Generator).
   * - :ref:`E1.C-12.2 <scenario-c-12>`
     - Logs of results are available for tracking the provenance of generated artifacts.
     - Artifacts were produced via the pipeline.
     - Implemented: Artifacts are produced as a result of the scans from pipeline execution and available for review.
   * - :ref:`E1.C-13.1 <scenario-c-13>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | SBOM artifact was produced.

       | Black Duck Polaris created an SBOM.

       | Endor Labs Reachability-Based SCA - SBOM Generation produced SBOM.

     - | Implemented: Artifacts (JSON and XML files) for the SBOM was produced and available for download and review within the pipeline artifact page.

       | Implemented: Black Duck Polaris also created an SBOM within the Polaris platform. In the Reporting tab, clicking on the Report filter brought up a list of Report Types. At the bottom of the list is the SBOM report, which can generate SPDX or CycloneDX report formats.

       | Implemented: Endor Labs Reachability-Based SCA - SBOM Generation produced the SBOM, which can be CycloneDX or SPDX format. Endor Labs can also ingest SBOMs in CycloneDX or SPDX format.
   * - :ref:`E1.C-13.2 <scenario-c-13>`
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - | SBOM artifact was produced.

       | DigiCert Software Trust Manager leveraged certificates to sign the SBOM.

     - | Implemented: SBOM is produced by AzDO and digitally signed.

       | Implemented: The pipeline was leveraged to sign the SBOM. After an SBOM was generated, a certificate from DigiCert Software Trust Manager was used to sign the SBOM.
   * - :ref:`E1.C-13.3 <scenario-c-13>`
     - Outputs are logged by the CI/CD pipeline.
     - | Microsoft AzDO CI/CD pipeline logged outputs as artifacts.

       | Black Duck Polaris produced an SBOM.

     - | Implemented: Artifacts (JSON and XML files) for the SBOM was produced and available for download and review within the pipeline artifact page.

       | Implemented: An SBOM is produced by Polaris.
   * - :ref:`E1.C-14.1 <scenario-c-14>`
     - Issues in container image software and configurations are identified.
     - | Container image findings are captured by Microsoft MDC.

       | Black Duck SCA performed container image scanning.

       | Endor Labs Container Scanning performed container image scanning.

     - | Implemented: Microsoft MDC provided the container findings specific to the artifact.

       | Implemented: Black Duck SCA scanned the container images.

       | Implemented: Endor Labs Container Scanning ran, and findings were captured and marked by criticality. As with other Endor Labs capabilities, detailed information is provided for each finding including risk details and remediation.
   * - :ref:`E1.C-14.2 <scenario-c-14>`
     - Source code and libraries are analyzed for defects, vulnerabilities, licensing issues, and code standard violations; outputs are logged.
     - | Output logs are provided in Microsoft MDC.

       | Black Duck Polaris and SCA scan were executed.

       | Endor Labs Reachability-Based SCA and Endor Code were executed for SAST and SCA scans.

     - | Implemented: Microsoft MDC provided the container findings specific to the artifact with criticality information.

       | Implemented: Black Duck Polaris and SCA analyzed and reported issues. Black Duck SCA scans augment Polaris SCA functionality to meet stringent third-party compliance and governance requirements. In the context of container images, Black Duck SCA distinguishes between code from base images vs that of the core application and performs deep license and copyright reviews.

       | Implemented: The pipeline, which integrated Endor Labs Endor Code and Reachability-Based SCA, provided findings and recommended remediations.
   * - :ref:`E1.C-14.3 <scenario-c-14>`
     - Logs of container scanner results, including issues, are produced.
     - | Output logs are provided in Microsoft MDC.

       | Logs of Black Duck outputs were created.

       | Logs of Endor Labs findings were created.

     - | Implemented: Microsoft MDC provided the container findings logs.

       | Implemented: Black Duck Polaris and Black Duck SCA provided logs of issues. Issues were updated via the Polaris and SCA integrations with SRM, which creates Work Items in AzDO.

       | Implemented: Endor Labs Endor Code and Reachability-Based SCA, provided findings and recommended remediations. All information can be exported.
   * - :ref:`E1.C-15.1 <scenario-c-15>`
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict the user.
   * - :ref:`E1.C-15.2 <scenario-c-15>`
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - Azure policies were applied to users.
     - | Implemented: Policies were implemented in Azure Entra ID and AzDO (within AzDO Teams and Permissions settings) to restrict certain users from accessing specific AzDO capabilities.
   * - :ref:`E1.C-15.3 <scenario-c-15>`
     - Infrastructure attributes (VMs, hosts, OS, etc.) meet the policy requirements and CI/CD pipelines are allowed to execute.
     - Microsoft Azure Policy used.
     - Implemented: Azure Policy can also be used to define and enforce policies for infrastructure to constrain what can be deployed by developers.
   * - :ref:`E1.C-15.4 <scenario-c-15>`
     - Secure communication is created between secrets/credential management tools and the build environment.
     - Integrations between AzDO tools and the build environment are secured.
     - Implemented: AzDO provided security for credentials management. Sentinel monitored issues within AzDO.
   * - :ref:`E1.C-15.5 <scenario-c-15>`
     - | Users with the required clearance can make changes to classified branches while those with lower clearance are denied access. Push and pull requests are logged for audit purposes.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - | Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.

       | Microsoft notes that using Entra ID, Microsoft AzDO and Azure policies can provide this capability although it does not define users by classification levels. For example, policies can be applied so that builds originating from unmanaged branches are not permitted for deployment into managed environments.
   * - :ref:`E1.C-15.6 <scenario-c-15>`
     - Merge requests should only succeed when the classification level requirements are met. Merge requests are logged for audit purposes.
     - N/A
     - | Not Implemented: Microsoft does not define users by classification levels. However, it can apply policies to merge requests based on certain
       | requirements.
   * - :ref:`E1.C-15.7 <scenario-c-15>`
     - System service accounts’ access to build systems and applications are allowed or denied based on ZT policies.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.C-15.8 <scenario-c-15>`
     - Build processes should only succeed when the container images are pulled from approved image registries specified in the ZT policies.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.C-15.9 <scenario-c-15>`
     - | Build artifacts are scanned for sensitive secrets before being allowed to leave the build process. Unapproved artifacts containing secrets not whitelisted by the ZT policies are prevented from leaving the build environment.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.C-15.10 <scenario-c-15>`
     - Trusted communication is enforced across build systems using certificate-based authentication.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.C-16.1 <scenario-c-16>`
     - Source code and configuration files are updated with generated changes and documented explanations.
     - Sagittal Neo generated source code, configuration, and documentation changes for projects hosted in Microsoft Azure DevOps.
     - | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Microsoft AzDO source code repositories.
   * - :ref:`E1.C-16.2 <scenario-c-16>`
     - Gaps and remediations for required standards are identified and provided as feedback.
     - | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

       | Black Duck AI Insights generated remediations based on standards and compliance findings detected in the Black Duck Polaris Platform.

     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.

       | Implemented: Black Duck AI Insights provides code suggestions and summary information based on SAST and SCA findings captured by Black Duck Polaris Platform components. Note: Black Duck AI Assist will provide suggestions and implementations based on user-provided context. AI Assist was not implemented as part of this demonstration.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.C-16.3 <scenario-c-16>`
     - Changes and explanations for external dependency risks are generated and documented.
     - | Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.

       | Black Duck AI Insights generated remediations based on software dependency findings detected in the Black Duck Polaris Platform.

     - | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output generated by Black Duck Software Risk Manager issue templates.

       | Implemented: Black Duck AI Insights provides code suggestions and summary information based on package or container image findings captured by Black Duck Polaris Platform components. Note: Black Duck AI Assist will provide suggestions and implementations based on user-provided context. AI Assist was not implemented as part of this demonstration.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.
   * - :ref:`E1.C-16.4 <scenario-c-16>`
     - Exposed secrets are identified, and feedback is provided to remediate improper storage or disclosure.
     - | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

       | Black Duck AI Insights generated code and configuration suggestions based on identified security and compliance findings.

     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.

       | Implemented: Black Duck AI Insights provides generated code suggestions and potential remediations based on linked security and compliance findings collected by Black Duck Polaris Platform. Note: Black Duck AI Assist will provide suggestions and implementations based on user-provided context. AI Assist was not implemented as part of this demonstration.

       | Note: Endor Labs AI Chat will provide suggestions and implementations based on user-provided context. AI Chat was not implemented as part of this demonstration.

.. _e1-test-results:

E1 Test Phase
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.D-1.1 <scenario-d-1>`
     - The test environment is provisioned, so that the updated software can be tested.
     - The CI/CD pipeline provisioned the test environment.
     - | Implemented: The Test environment is provisioned, including the CI/CD pipeline is provisioned. Note that SCM and configuration management capabilities are included in AzDO.
   * - :ref:`E1.D-1.2 <scenario-d-1>`
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - | The CI/CD pipeline ran various security scans.

       | Black Duck Polaris and SCA scans were executed.

       | Endor Labs Endor Code and Reachability-Based SCA scans were executed.

     - | Implemented: the CI/CD pipeline ran various security scans in the “Test” stage of the pipeline.

       | Implemented: The pipeline, which integrated Black Duck Polaris’s SAST and SCA capabilities, identified vulnerabilities. These vulnerabilities can then be reported back to AzDO for remediation.

       | Implemented: The pipeline, which integrated Endor Labs Endor Code and Reachability-Based SCA, provided findings and recommended remediations.
   * - :ref:`E1.D-1.3 <scenario-d-1>`
     - | Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the test process.
     - | AzDO logged results of the CI/CD Pipeline outputs.

       | Black Duck SRM was integrated with AzDO to update Work Items.

     - | Implemented: raw logs are available for “Test” stage of the pipeline.

       | Implemented: Remediation issues were updated in AzDO Work Items from Black Duck via SRM.
   * - :ref:`E1.D-1.4 <scenario-d-1>`
     - The resources used for the test environment have been freed up – no VMs, Containers, tools, or other environment components are still provisioned.
     - AzDO pipelines performed “clean up” tasks.
     - | Implemented: When resources are no longer used, the CI/CD pipeline performed functions to free up the resources in the environment. These steps were configured in the end of the pipeline execution.
   * - :ref:`E1.D-2 <scenario-d-2>`
     - Refer to results for E1.C3.
     - Refer to results for E1.C3.
     - Refer to results for E1.C3.
   * - :ref:`E1.D-3.1 <scenario-d-3>`
     - SCA identifies security vulnerabilities and compliance issues before third-party artifacts are used.
     - | Vulnerabilities were identified in AzDO Advanced Security.

       | Black Duck Polaris and Black Duck SCA scans were executed.

       | Endor Labs Endor Reachability-Based SCA scans executed.

     - | Implemented: The CI/CD pipeline for the test phase executed SCA tool (e.g., GHAzDO).

       | Implemented: Black Duck Polaris and Black Duck SCA capabilities identified risky 3\ :sup:`rd` party libraries. Black Duck SCA scans augment Polaris SCA functionality to meet stringent 3\ :sup:`rd` party compliance and governance requirements. In the context of 3\ :sup:`rd` party validation workflows, Black Duck SCA provides component intelligence covering the capabilities within a library, including authorship provenance and cryptographic capabilities.

       | Implemented: Endor Labs Endor Reachability-Based SCA provided findings and recommended remediations.
   * - :ref:`E1.D-3.2 <scenario-d-3>`
     - SAST identifies security vulnerabilities and compliance issues before internal artifacts can be used.
     - | Vulnerabilities were identified in AzDO Advanced Security.

       | Vulnerabilities were identified in Black Duck Polaris SAST.

       | Endor Labs Endor Code provided SAST scans.

     - | Implemented: GHAzDO provided findings and results are provided in the summary page of the pipeline and vulnerabilities for the tools were provided in the Advanced Security page under the Repos tab.

       | Implemented: Black Duck Polaris’s SAST capabilities identified vulnerabilities. Vulnerabilities within internal codebases can be assessed against standardized compliance reports or policies to ensure that code from independent internal teams meet release criteria for end products.

       | Implemented: Endor Labs Endor Code provided findings and recommended remediations to SAST scans.
   * - :ref:`E1.D-3.3 <scenario-d-3>`
     - Issues are created in the ticketing system and logs of changes are maintained.
     - | AzDO ticketing tool was used to track issues.

       | Polaris was integrated with AzDO to report findings.

     - | Implemented: In this build we leveraged AzDO Boards and Work Items for ticketing issues.

       | Implemented: Vulnerabilities identified by Polaris were reported back to AzDO for remediation via Work Items.
   * - :ref:`E1.D-4.1 <scenario-d-4>`
     - Unit tests are pulled from SCM and ran successfully against known functional criteria.
     - CI/CD pipeline is configured to run all unit tests for the app.
     - Implemented: The CI/CD pipeline for the test phase successfully ran the unit tests.
   * - :ref:`E1.D-4.2 <scenario-d-4>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results including issues (e.g., defects) in the ticketing system.
     - Outputs are recorded by the pipeline.
     - Implemented: test outputs are logged and AzDO provides raw logs for detailed information.
   * - :ref:`E1.D-5.1 <scenario-d-5>`
     - Regression test scripts are pulled from SCM and run successfully against known regression criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-5.2 <scenario-d-5>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-6.1 <scenario-d-6>`
     - Integration test scripts are pulled from SCM and run successfully against known integration criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-6.2 <scenario-d-6>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-7.1 <scenario-d-7>`
     - Acceptance test scripts are pulled from SCM and run successfully against known acceptance criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-7.2 <scenario-d-7>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-8.1 <scenario-d-8>`
     - Smoke test scripts are pulled from SCM and run successfully against known smoke test criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-8.2 <scenario-d-8>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-9.1 <scenario-d-9>`
     - DAST tests are run successfully against security criteria.
     - Black Duck Dynamic, part of Polaris, performed DAST testing.
     - | Implemented: The Black Duck Polaris platform, specifically Dynamic (DAST) scanning, was integrated into the CI/CD pipeline and performed DAST testing. In addition to traditional DAST, Polaris Dynamic, assesses an application’s APIs when generating test cases.
   * - :ref:`E1.D-9.2 <scenario-d-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - | AzDO provided logs.

       | Black Duck was integrated with AzDO to provide logs/results of scans.

     - | Implemented: Logs were reported in AzDO Advanced Security under the Repos tab.

       | Implemented: Results of the DAST testing were logged. SRM was leveraged to create Work Items in AzDO for remediation.
   * - :ref:`E1.D-9.3 <scenario-d-9>`
     - Output of report is inspected for vulnerability severity (e.g., CVE/CVSS score).
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-10.1 <scenario-d-10>`
     - Acceptance or Integration test scripts are pulled from SCM and run successfully against known integration criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-10.2 <scenario-d-10>`
     - IAST is run successfully against known security criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-10.3 <scenario-d-10>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-11.1 <scenario-d-11>`
     - Fuzz testing is run successfully.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-11.2 <scenario-d-11>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-12.1 <scenario-d-12>`
     - API testing is run successfully.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-12.2 <scenario-d-12>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.D-13.1 <scenario-d-13>`
     - The pipeline stops when the code violates the policy.
     - Violation of code policy was logged for review.
     - | Implemented: While the expected outcome calls for the stoppage of the pipeline, we only logged the violations for the purposes of this demonstration so that we have the pipeline continue to run next steps.
   * - :ref:`E1.D-13.2 <scenario-d-13>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - CI/CD pipeline logged outputs.
     - Implemented: Test artifacts are published in “Test” stage execution of the pipeline.
   * - :ref:`E1.D-14.1 <scenario-d-14>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.D-14.2 <scenario-d-14>`
     - Logs of firmware updates or changes are captured
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.D-15.1 <scenario-d-15>`
     - Software components are digitally signed, and secrets are stored and protected by HSM.
     - | Artifacts are signed in AzDO.

       | DigiCert Software Trust Manager was leveraged to manage and protect sensitive information.

     - | Partially implemented: Generated containers and packaged artifacts are configured to be digitally signed with a cryptographic hash function. No HSM is available for this demonstration.

       | Implemented: DigiCert Software Trust Manager securely manages key pairs and certificates to sign software components including binaries and artifacts. Where DigiCert was used for the demonstration, a FIPS compliant shared HSM was used in this implementation where public certs were used. DigiCert Software Trust Manager also leveraged a self-hosted soft HSM for self-signed certs and key pairs.
   * - :ref:`E1.D-15.2 <scenario-d-15>`
     - Signed software components are authentic and not tampered with.
     - | Artifacts were signed with cryptographic hash function.

       | DigiCert Software Trust Manager was leveraged to manage and protect sensitive information.

     - | Implemented: AzDO leveraged cryptographic hash functions to ensure that the artifacts are not tampered with.

       | Implemented: DigiCert Software Trust Manager was integrated with AzDO and proper credentials were set up so that certificates and key pairs were securely retrieved from Software Trust Manager. The pipeline executed the tasks to sign the SBOM.
   * - :ref:`E1.D-15.3 <scenario-d-15>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - AzDO provided logs.
     - Implemented: Hash information can be retrieved from Azure. Alerting capabilities are not available for this demonstration.
   * - :ref:`E1.D-16.1 <scenario-d-16>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - This demonstration has been deferred to a future example implementation.
     - | This demonstration has been deferred to a future example implementation.

       | Note: Microsoft AzDO Marketplace extensions can generate SLSA provenance artifacts (for example, Xygeni Build Attestation; SLSA Provenance Generator).

   * - :ref:`E1.D-16.2 <scenario-d-16>`
     - Logs of results are available for tracking the integrity of the supply chain.
     - Artifacts were produced via the pipeline.
     - Implemented: Artifacts are produced from the scans from the pipeline execution and available for review.
   * - :ref:`E1.D-17.1 <scenario-d-17>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | SBOM artifact was produced.

       | SBOM was created in Black Duck Polaris.

       | SBOM was created in Endor Labs Reachability-Based SCA - SBOM Generation.

     - | Implemented: Artifacts (JSON and XML files) for the SBOM was produced and available for download and review within the pipeline artifact page.

       | Implemented: Black Duck Polaris was able to produce an SBOM. In the Reporting tab, clicking on the Report filter brought up a list of Report Types. At the bottom of the list is the SBOM report.

       | Implemented: SBOMs were created in Endor Labs and can be exported.
   * - :ref:`E1.D-17.2 <scenario-d-17>`
     - Confirm SBOM signatures to verify authenticity and integrity of all soft-ware artifacts.
     - | SBOM artifact was produced.

       | DigiCert Software Trust Manager leveraged certificates to sign the SBOM.

     - | Implemented: After an SBOM was generated, a certificate from DigiCert Software Trust Manager was used to sign the SBOM. We confirmed that the signed SBOM matched the signature provided by the Software Trust Manager (in the logs section.)
   * - :ref:`E1.D-17.3 <scenario-d-17>`
     - Outputs are logged by the CI/CD pipeline.
     - AzDO CI/CD pipeline logged outputs as artifacts.
     - Implemented: Artifacts (JSON and XML files) for the SBOM was produced and available for download and review within the pipeline artifact page.
   * - :ref:`E1.D-18.1 <scenario-d-18>`
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict users.
   * - :ref:`E1.D-18.2 <scenario-d-18>`
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO (within AzDO Teams and Permissions settings) to restrict certain users from accessing specific AzDO capabilities.
   * - :ref:`E1.D-18.3 <scenario-d-18>`
     - | Update ZT solutions to apply policies to the DevSecOps infrastructure (e.g., VMs, host, OS’s, etc.) so that the CI/CD pipelines will run only if infrastructure meets policy requirements.
     - Microsoft Azure Policy used.
     - Implemented: Azure Policy can also be used to define and enforce policies for infrastructure to constrain what can be deployed by developers.
   * - :ref:`E1.D-18.4 <scenario-d-18>`
     - Secure communication is created between secret/credential management tools and the build environment.
     - Integrations between Microsoft AzDO tools, AKV, and the build environment are secured.
     - | Implemented: Microsoft AzDO provided security for credentials management. Microsoft AKV securely stored secrets. Policies were configured to provide secure communication between AKV, the Test environment, and AzDO. Sentinel monitored issues within AzDO.
   * - :ref:`E1.D-18.5 <scenario-d-18>`
     - Failing mandatory tests specified in ZT policies are blocked from advancing.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.D-18.6 <scenario-d-18>`
     - Test Phase communications are secured using certificate-based authentication.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.D-18.7 <scenario-d-18>`
     - If keywords are detected in job logs an incident report is created.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.D-18.8 <scenario-d-18>`
     - CI/CD pipeline progression is blocked based on vulnerabilities found in security reports.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.D-19.1 <scenario-d-19>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - Sagittal Neo generated remediations from feedback provided by failed testing actions.
     - Implemented: Sagittal Neo provides source code and configuration changes based detected failures captured by testing components during this phase.
   * - :ref:`E1.D-19.2 <scenario-d-19>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.D-19.3 <scenario-d-19>`
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.
     - | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.D-19.4 <scenario-d-19>`
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - Sagittal Neo generated remediations from feedback provided by failed testing actions.
     - Implemented: Sagittal Neo provides source code and configuration changes based on detected test failures and generated reports.
   * - :ref:`E1.D-19.5 <scenario-d-19>`
     - Performance bottlenecks are identified, and optimizations are provided.
     - Demonstrations of performance monitoring and assessment are out of scope of example implementations.
     - Demonstrations of performance monitoring and assessment are out of scope of example implementations.
   * - :ref:`E1.D-19.6 <scenario-d-19>`
     - Security findings are summarized with actionable mitigation steps.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.

.. _e1-release-results:

E1 Release Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 40 63

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.E-1.1 <scenario-e-1>`
     - The release environment is provisioned, so that the updated software can be released.
     - The CI/CD pipeline provisioned the test environment.
     - Implemented: The Test environment including the CI/CD pipeline is provisioned. SCM and configuration management capabilities are included in AzDO.
   * - :ref:`E1.E-1.2 <scenario-e-1>`
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - | The CI/CD pipeline ran various security scans.

       | Black Duck Polaris and SCA scans were executed.

     - | Implemented: the CI/CD pipeline ran various security scans in the “Release” stage of the pipeline.

       | Implemented: The pipeline, which integrated Black Duck Polaris’s SAST and SCA capabilities, identified vulnerabilities. These vulnerabilities can then be reported back to AzDO for remediation.
   * - :ref:`E1.E-1.3 <scenario-e-1>`
     - | Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the Release process.
     - AzDO logged results of the CI/CD Pipeline outputs
     - Implemented: raw logs are available for the “Release” stage of the pipeline.
   * - :ref:`E1.E-2.1 <scenario-e-2>`
     - Artifacts created in this phase are securely stored in the Release phase artifact repository.
     - A repository was created for the release phase artifacts.
     - Implemented: the “Release” stage of the pipeline published release.
   * - :ref:`E1.E-2.2 <scenario-e-2>`
     - Outputs are logged and artifacts can be released.
     - AzDO CI/CD pipeline execution steps are logged.
     - Implemented: raw logs are available for the “Release” stage of the pipeline.
   * - :ref:`E1.E-3.1 <scenario-e-3>`
     - Information (e.g., certificates, credentials, and secrets; configuration versions) is maintained and secured by management systems.
     - AzDO leveraged a credential management system to manage sensitive information.
     - Implemented: The CI/CD pipeline leveraged akvServiceConnection for credential management.
   * - :ref:`E1.E-3.2 <scenario-e-3>`
     - Logs and incidents are recorded.
     - AzDO pipeline executions are logged
     - Implemented: All pipeline executions are logged.
   * - :ref:`E1.E-4.1 <scenario-e-4>`
     - Release packages are completed for distribution.
     - AzDO published the release package
     - Implemented: the “Release” stage of the pipeline published the artifacts in the Release repository.
   * - :ref:`E1.E-4.2 <scenario-e-4>`
     - | Artifacts are organized, tracked, and secured. Software dependencies; Licensing analysis results; Bugs or defects; Security vulnerabilities

       | All software, including code, tools, and 3rd party libraries are running with the correct or expected versions.

     - AzDO produced outputs of artifacts for each stage.
     - | Implemented: Outputs of artifacts are provided in the pipeline execution. Note that only approved users have access to the information. Artifacts can be downloaded from AzDO.
   * - :ref:`E1.E-5.1 <scenario-e-5>`
     - Release information is collected and documented; Software dependencies, images, binaries, and software libraries are validated.
     - Release information is published in Azure Artifacts.
     - Implemented: Release pipeline performed validation of the software, published release data, and authenticated to Azure Artifacts feed.
   * - :ref:`E1.E-5.2 <scenario-e-5>`
     - Audit logs and compliance information are documented and provided to stakeholders.
     - Audit logs and compliance information are published to CI/CD pipeline logs. Notifications of failures are visible in AzDO Pipelines.
     - Implemented: All pipeline executions are logged. Stakeholders can see status and view logs via notifications in AzDO interface.
   * - :ref:`E1.E-6.1 <scenario-e-6>`
     - The results from the testing phase are gathered and put with the release.
     - AzDO performed this function.
     - Implemented: AzDO CI/CD pipeline leveraged the output of the software from the test phase to perform release functions.
   * - :ref:`E1.E-7.1 <scenario-e-7>`
     - Smoke test scripts are pulled from SCM and run successfully against known smoke test criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-7.2 <scenario-e-7>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-8.1 <scenario-e-8>`
     - Acceptance test scripts are pulled from SCM and run successfully against known acceptance criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-8.2 <scenario-e-8>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-9.1 <scenario-e-9>`
     - DAST tests are run successfully against security criteria.
     - | Microsoft GHAzDO ran DAST tests.

       | Black Duck Dynamic, part of Polaris, performed DAST testing.

     - | N/A: Azure currently does not perform DAST tests.

       | Implemented: Black Duck Polaris platform, specifically Dynamic testing (DAST), was integrated into the CI/CD pipeline and performed DAST testing.
   * - :ref:`E1.E-9.2 <scenario-e-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - | AzDO provided logs.

       | Black Duck was integrated with AzDO to provide logs/results of scans.

     - | Implemented: Logs were reported in AzDO Advanced Security under the Repos tab.

       | Implemented: Results of the DAST testing were logged. SRM was leveraged to create Work Items in AzDO for remediation.
   * - :ref:`E1.E-9.3 <scenario-e-9>`
     - Acceptance test scripts are pulled from SCM and run successfully against known integration criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-9.4 <scenario-e-9>`
     - IAST is run successfully against known security criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-9.5 <scenario-e-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E1.E-10.1 <scenario-e-10>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.E-10.2 <scenario-e-10>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.E-11.1 <scenario-e-11>`
     - | Software components and artifacts (e.g., commits, images, binaries, or libraries; Signature files) are digitally signed and secrets are stored and protected by HSM.
     - | Microsoft AzDO leveraged AKV for secrets.

       | DigiCert Software Trust Manager was leveraged to manage and protect sensitive information.

     - | Implemented: AzDO Pipelines leveraged Service Connections for credential management including secure storage.

       | Note: Microsoft AKV supports HSM-backed keys (Managed HSM), integrate Microsoft AzDO with AKV (via MDP) for secrets management and secret/key injection. The current subscription of AzDO does not have an HSM to store certificates and other secrets.

       | Implemented: DigiCert Software Trust Manager securely manages key pairs and certificates to sign software components including binaries and artifacts. An HSM was used for storage. Refer to E1.B-5.3 about details of HSMs.
   * - :ref:`E1.E-11.2 <scenario-e-11>`
     - Results confirm that software components and artifacts are authentic and not tampered with.
     - | AzDO confirmed authentication of artifacts.

       | DigiCert Software Trust Manager was leveraged to manage and protect sensitive information.

     - | Implemented: AzDO Release stage pipeline performed authentication of artifacts with logs.

       | Implemented: DigiCert Software Trust Manager was integrated with AzDO, and proper credentials were set up so that certificates and key pairs were securely retrieved from Software Trust Manager.
   * - :ref:`E1.E-11.3 <scenario-e-11>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - | Logs captured in AzDO

       | Black Duck Polaris SCA scans were executed.

     - | Partially implemented: Logs were created but no alerting capabilities are available in this demonstration.

       | Partially implemented: Results of SCA scans were provided back AzDO in Work Items for remediation. There was no integration with a tool to alert stakeholders, refer to prior notes.
   * - :ref:`E1.E-12.1 <scenario-e-12>`
     - Issues in container image software and configurations are identified.
     - | Container image findings are captured by Microsoft MDC.

       | Black Duck SCA performed container image scans.

       | Endor Labs Container Scanning was performed.

     - | Implemented: Microsoft MDC provided the container findings specific to the artifact.

       | Implemented: The pipeline ran the container image scans from the Black Duck tools.

       | Implemented: Endor Labs Container Scanning was integrated with AzDO and initiated via endorctl via the CI/CD pipeline.
   * - :ref:`E1.E-12.2 <scenario-e-12>`
     - Source code and libraries are analyzed for defects, vulnerabilities, licensing issues, and code standard violations; outputs are logged.
     - | Output logs are provided in Microsoft MDC.

       | Logs provided by Black Duck SRM.

       | Logs provided by Endor Labs website.

     - | Implemented: Microsoft MDC provided the container findings specific to the artifact with criticality information.

       | Implemented: The  pipeline ran SAST and SCA scans from the Black Duck tools.

       | Implemented: All logs were captured and viewable per the project related to the AzDO CI/CD pipeline that initiated the scan.
   * - :ref:`E1.E-12.3 <scenario-e-12>`
     - Logs of container scanner results, including issues, are produced.
     - | Output logs are provided in Microsoft MDC.

       | Black Duck produced outputs.

       | Logs provided by Endor Labs website.

     - | Implemented: Microsoft MDC provided the container findings logs.

       | Implemented: Scan results from Black Duck were provided. Issues were then created as Work Items in AzDO through the integration of SRM.

       | Implemented: All logs were captured and viewable per the project related to the AzDO CI/CD pipeline that initiated the scan. It can also be exported.
   * - :ref:`E1.E-12.4 <scenario-e-12>`
     - Images meeting security criteria are accepted.
     - Image is accepted and used for the next phase.
     - Implemented: In this sample demonstration, we accepted the image even though there were issues to demonstrate the process.
   * - :ref:`E1.E-13.1 <scenario-e-13>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - This demonstration has been deferred to a future example implementation.
     - | This demonstration has been deferred to a future example implementation.

       | Note: Microsoft AzDO Marketplace extensions can generate SLSA provenance artifacts (for example, Xygeni Build Attestation; SLSA Provenance Generator). 
   * - :ref:`E1.E-13.2 <scenario-e-13>`
     - Logs of results are available for tracking the integrity of the supply chain.
     - Artifacts were produced via the pipeline.
     - Implemented: Artifacts are produced as a result of the scans from the pipeline execution and available for review.
   * - :ref:`E1.E-13.3 <scenario-e-13>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | SBOM artifact was produced.

       | Black Duck Polaris produced an SBOM.

     - | Implemented: Artifacts (JSON and XML files) for the SBOM were produced and available for download and review within the pipeline artifact page.

       | Implemented: Black Duck was able to produce an SBOM from the software packages it scanned.
   * - :ref:`E1.E-13.4 <scenario-e-13>`
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - | SBOM artifact was produced.

       | DigiCert Software Trust Manager leveraged certificates to sign the SBOM.

     - Implemented: After an SBOM was generated, a certificate from DigiCert Software Trust Manager was used to sign the SBOM.
   * - :ref:`E1.E-13.5 <scenario-e-13>`
     - Outputs are logged by the CI/CD pipeline.
     - AzDO CI/CD pipeline logged outputs as artifacts.
     - Implemented: Artifacts (JSON and XML files) for the SBOM were produced and available for download and review within the pipeline artifact page.
   * - :ref:`E1.E-14.1 <scenario-e-14>`
     - IaC Scanner identifies security vulnerabilities and compliance issues before IaC is executed.
     - | AzDO scanned IaC scripts prior to execution.

       | Black Duck Polaris performed IaC scanning.

       | Endor Labs Endor Code scanned for IaC vulnerabilities.

     - | Implemented: AzDO Advanced Security ran several IaC scanner tools (e.g., iacfilescanner, checkov, and templateanalyzer) and identified vulnerabilities.
       | This was executed in the pipeline.

       | Implemented: Through the CI/CD pipeline, Black Duck Polaris scanned the IaC (k8s).

       | Implemented: Endor Labs Endor Code scanned for IaC vulnerabilities. Results of vulnerabilities are logged with risk details and remediation information.
   * - :ref:`E1.E-14.2 <scenario-e-14>`
     - Issues are created and resolved, and logs of changes are maintained.
     - | Issues logged in AzDO and updates made to resolve issues.

       | Black Duck records findings and passes it back to AzDO.

     - | Implemented: The pipeline ran the tools and logged the issues. Issues were resolved.

       | Implemented: Issues found by Black Duck were provided back to AzDO by leveraging SRM to create Work Items.
   * - :ref:`E1.E-14.3 <scenario-e-14>`
     - Release environment is provisioned and managed based on scanned IaC artifacts to ensure consistency.
     - Build environment is provision via a separate pipeline.
     - Implemented: The pipeline ensures consistency of the Release environment.
   * - :ref:`E1.E-15.1 <scenario-e-15>`
     - Users’ access to release systems and applications are allowed or denied based on ZT policies.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict the user.
   * - :ref:`E1.E-15.2 <scenario-e-15>`
     - Infrastructure meets the policy requirements and tools are allowed to execute.
     - Microsoft Azure Policy leveraged.
     - Implemented: Azure Policy can also be used to define and enforce policies for infrastructure to constrain what can be deployed by developers.
   * - :ref:`E1.E-15.3 <scenario-e-15>`
     - | Update policies in ZT solution tools to ensure release and deployment secrets, credentials, and variables certificates, credentials, and secrets stored on the file system are secured.
     - Microsoft AzDO, AKV, and the Release phase environment are securely integrated.
     - | Implemented: Multiple security capabilities are leveraged to ensure Microsoft AKV communications are secured, identity and access controls are applied.
       | Authentication is configured between Microsoft AzDO and AKV. Other policies were configured to secure communication between AKV and the VNets.
   * - :ref:`E1.E-15.4 <scenario-e-15>`
     - Only software proven to originate from the approved build and test phase processes in compliance with ZT policies are staged for release.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.E-16.1 <scenario-e-16>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - Sagittal Neo generated remediations from feedback provided by failed release actions.
     - Implemented: Sagittal Neo provides source code and configuration changes based detected failures captured by release components during this phase.
   * - :ref:`E1.E-16.2 <scenario-e-16>`
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - Sagittal Neo generated remediations from feedback provided by failed release actions.
     - Implemented: Sagittal Neo provides source code and configuration changes based on detected test failures and generated reports.
   * - :ref:`E1.E-16.3 <scenario-e-16>`
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.
     - | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.E-16.4 <scenario-e-16>`
     - | Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or credentials.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.E-16.5 <scenario-e-16>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.E-16.6 <scenario-e-16>`
     - Plans are generated and provide methods to mitigate or remediate vulnerabilities found in artifacts.
     - Sagittal Neo generated source code, configuration, and documentation changes for projects hosted in Microsoft Azure DevOps.
     - | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Microsoft AzDO source code repositories.

.. _e1-deploy-results:

E1 Deploy Phase
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.F-1.1 <scenario-f-1>`
     - The deployment environment is provisioned, so that the updated software can be deployed.
     - The CI/CD pipeline provisioned the test environment.
     - Implemented: The Deploy environment, including the CI/CD pipeline is provisioned.
   * - :ref:`E1.F-1.2 <scenario-f-1>`
     - CI/CD Pipelines run all deployment process components, and each component generates output for tracking status and logging detailed information.
     - The CI/CD pipeline ran various security scans.
     - Implemented: the “Deploy” stage of the CI/CD pipeline ran various security scans in the “Deploy” stage of the pipeline.
   * - :ref:`E1.F-1.3 <scenario-f-1>`
     - | Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track configuration status and detailed information about the Release process.
     - AzDO logged results of the CI/CD Pipeline outputs
     - Implemented: raw logs are available for the “Deploy” stage of the pipeline.
   * - :ref:`E1.F-2 <scenario-f-2>`
     - Refer to results of E1.E-2.
     - Refer to results of E1.E-2.
     - Refer to results of E1.E-2.
   * - :ref:`E1.F-3 <scenario-f-3>`
     - Refer to results of E1.E-3.
     - Refer to results of E1.E-3.
     - Refer to results of E1.E-3.
   * - :ref:`E1.F-4 <scenario-f-4>`
     - Refer to results of E1.E-5.
     - Refer to results of E1.E-5.
     - Refer to results of E1.E-5.
   * - :ref:`E1.F-5 <scenario-f-5>`
     - Refer to results of E1.E-14.
     - Refer to results of E1.E-14.
     - Refer to results of E1.E-14.
   * - :ref:`E1.F-6.1 <scenario-f-6>`
     - SBOM and other provenance data are verified before deployment.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.F-6.2 <scenario-f-6>`
     - | Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the SBOM process.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.F-7.1 <scenario-f-7>`
     - Results confirm that firmware components and artifacts are authentic and not tampered with.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.F-7.2 <scenario-f-7>`
     - Software components and artifacts that are verified are accepted.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.F-7.3 <scenario-f-7>`
     - Firmware is up to date on all hardware components.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.F-8.1 <scenario-f-8>`
     - Users’ access to the deploy phase environment are allowed or denied based on ZT policies.
     - Azure policies were applied to users.
     - Implemented: Policies were implemented in Azure Entra ID and AzDO to restrict users.
   * - :ref:`E1.F-8.2 <scenario-f-8>`
     - System-to-system communications are restricted based on functionality and ZT policies.
     - Microsoft Entra ID and Azure Policy leveraged to secure communications.
     - | Implemented: Entra ID provided the role base access, leveraging service principles – for secure service to service communication. Azure Policy can also be used to define and enforce policies for infrastructure to constrain what can be deployed by developers.
   * - :ref:`E1.F-8.3 <scenario-f-8>`
     - Only software proven to originate from the approved build and test phase processes are deployed.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.F-8.4 <scenario-f-8>`
     - Only software that meets data residency requirements are deployed.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.F-9.1 <scenario-f-9>`
     - Suggestions and remediation guidance are provided and documented for the identified deployment issues.
     - Sagittal Neo generated remediations from feedback provided by failed deployment activities.
     - Implemented: Sagittal Neo provides source code and configuration changes based detected failures captured by deployment components during this phase.
   * - :ref:`E1.F-9.2 <scenario-f-9>`
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - Sagittal Neo provided analysis of risks and vulnerabilities provided as context from Black Duck Software Risk Manager issue templates.
     - | Implemented: Sagittal Neo provides generated content based on associated security requirements included work items created by the Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.F-9.3 <scenario-f-9>`
     - Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.F-9.4 <scenario-f-9>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.
   * - :ref:`E1.F-9.5 <scenario-f-9>`
     - Configuration changes are generated in configuration management system.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.F-9.6 <scenario-f-9>`
     - Deployment status and scope notifications are generated and documented in project or deployment management systems.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.

.. _e1-operate-results:

E1 Operate Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.G-1 <scenario-g-1>`
     - Refer to results for E1.F-1
     - Refer to results for E1.F-1
     - Refer to results for E1.F-1
   * - :ref:`E1.G-2 <scenario-g-2>`
     - Refer to results for E1.F-7
     - Refer to results for E1.F-7
     - Refer to results for E1.F-7
   * - :ref:`E1.G-3 <scenario-g-3>`
     - Refer to results for E1.E-13
     - Refer to results for E1.E-13
     - Refer to results for E1.E-13
   * - :ref:`E1.G-4.1 <scenario-g-4>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.G-4.2 <scenario-g-4>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.G-4.3 <scenario-g-4>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.G-5.1 <scenario-g-5>`
     - Users’ access to the operate phase environment are allowed or denied based on ZT policies
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.
   * - :ref:`E1.G-5.2 <scenario-g-5>`
     - System-to-system communications are restricted based on functionality and ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized systems, users, and service accounts.

       | Microsoft Azure Network Security Groups were implemented to restrict network communication within the operate phase environment.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provide role-based access control and policies alongside network and resource access controls to restrict system and resource communications within an environment.
   * - :ref:`E1.G-5.3 <scenario-g-5>`
     - Unauthorized changes and vulnerabilities are detected and reported based on the ZT policies.
     - | Microsoft Azure Entra ID provided policy management of service accounts and other service principals.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized systems and service accounts.

     - Partially Implemented: Microsoft Azure Entra ID and Conditional Access policies were implemented; however, detection and reporting automation was not implemented at the application-level for this example implementation.
   * - :ref:`E1.G-6.1 <scenario-g-6>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - Sagittal Neo generated remediations from feedback provided by failed operational actions.
     - Implemented: Sagittal Neo provides source code and configuration changes based detected failures captured by operational components during this phase.
   * - :ref:`E1.G-6.2 <scenario-g-6>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output generated by Black Duck Software Risk Manager issue templates.

.. _e1-continuous-improvements-results:

E1 Continuous Improvements, Security and Monitoring Phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 40 63

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E1.H-1 <scenario-h-1>`
     - Refer to results for E1.A-5-7, E1.A-6, E1.A-7, E1.F-1, and E1-F-3
     - Refer to results for E1.A-5-7, E1.A-6, E1.A-7, E1.F-1, and E1-F-3
     - Refer to results for E1.A-5-7, E1.A-6, E1.A-7, E1.F-1, and E1-F-3
   * - :ref:`E1.H-2 <scenario-h-2>`
     - Refer to results for E1.A-1
     - Refer to results for E1.A-1
     - Refer to results for E1.A-1
   * - :ref:`E1.H-3.1 <scenario-h-3>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Microsoft Azure Log Analytics,

       | Microsoft MDC, and Microsoft Sentinel used for monitoring.

     - | Implemented: For application monitoring, the combination of the Azure components provided logs and monitoring capabilities to the AzDO software.
       | Microsoft MDC provided Workload protection and DevOps security. Logs from Log Analytics and Sentinel were used for monitoring as well.
   * - :ref:`E1.H-3.2 <scenario-h-3>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Microsoft Azure Log Analytics,

       | Microsoft MDC, and Microsoft Sentinel used for monitoring.

     - | Implemented: For network monitoring, the combination of the Azure components provided logs and monitoring capabilities to the networks used for Azure and
       | AzDO components. MDC provided Network security. Logs from Log Analytics and Sentinel were used for monitoring as well.
   * - :ref:`E1.H-4.1 <scenario-h-4>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Microsoft Azure Log Analytics,

       | Microsoft MDC, and Microsoft Sentinel used for monitoring.

     - | Implemented: For security monitoring, the combination of the Azure components provided logs and monitoring capabilities to the networks used for Azure and AzDO components. MDC provided Cloud security, which contains various security monitoring capabilities such as workload, data, DevOps, and posture. Logs from Log Analytics and Sentinel were used for monitoring as well.
   * - :ref:`E1.H-4.2 <scenario-h-4>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - Microsoft Azure Log Analytics, Microsoft MDC, and Microsoft Sentinel were used for monitoring.
     - Partially Implemented: Security monitoring, cloud security, logging and continuous monitoring were implemented using MDC, Sentinel, and Azure Log Analytics. Automated heuristics of newly discovered infrastructure or application vulnerabilities were not implemented as part of this example implementation.
   * - :ref:`E1.H-4.3 <scenario-h-4>`
     - The responsible disclosure of new vulnerabilities discovered by external sources.
     - Demonstration of process for disclosure of undiscovered vulnerabilities is out of scope of example implementations.
     - Demonstration of process for disclosure of undiscovered vulnerabilities is out of scope of example implementations.
   * - :ref:`E1.H-5.1 <scenario-h-5>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.H-5.2 <scenario-h-5>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.H-5.3 <scenario-h-5>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E1.H-6.1 <scenario-h-6>`
     - Refer to results for E1. F-9.1
     - Refer to results for E1. F-9.1
     - Refer to results for E1. F-9.1
   * - :ref:`E1.H-6.2 <scenario-h-6>`
     - Refer to results for E1.F-9.2
     - Refer to results for E1.F-9.2
     - Refer to results for E1.F-9.2
   * - :ref:`E1.H-6.3 <scenario-h-6>`
     - Refer to results for E1.B-10.3
     - Refer to results for E1.B-10.3
     - Refer to results for E1.B-10.3
   * - :ref:`E1.H-6.4 <scenario-h-6>`
     - Refer to results for E1.C-15.3
     - Refer to results for E1.C-15.3
     - Refer to results for E1.C-15.3
   * - :ref:`E1.H-6.5 <scenario-h-6>`
     - Refer to results for E1.E-15.3
     - Refer to results for E1.E-15.3
     - Refer to results for E1.E-15.3
   * - :ref:`E1.H-6.6 <scenario-h-6>`
     - Unauthorized changes are detected and reported.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
     - Scenario not available during Example Implementation 1 – This demonstration was added in Example Implementation 2.
   * - :ref:`E1.H-7.1 <scenario-h-7>`
     - Risk reports are generated, and mitigation actions are triggered in risk management or ticketing systems.
     - Sagittal Neo provided analysis of standards and frameworks provided as context.
     - | Implemented: Sagittal Neo provides generated content based on associated security compliance requirements included in assigned work items in Microsoft AzDO Boards.
   * - :ref:`E1.H-7.2 <scenario-h-7>`
     - Security alerts are correlated with logs, and corresponding remediation tickets are automatically generated.
     - Sagittal Neo provided analysis of standards and frameworks provided as context.
     - | Implemented: Sagittal Neo provides generated content based on associated security compliance requirements included in assigned work items in Microsoft AzDO Boards.

Example Implementation 2 (E2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes the functional demonstration results for the example implementation 2. 


.. _e2-plan-results:

E2 Plan Phase
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.A-1.1 <scenario-a-1>`
     - Users have access to the collaboration tools, project plan, workflows, and assigned tasks.
     - GitLab Platform provided Epics, Issues, and Tasks for planning, organized with Labels, Milestones, and Iterations, and visualized on Boards and Roadmaps.
     - | Implemented: Work is broken down through Epics, Issues, and Tasks, categorized with Labels, scheduled across Milestones and Iterations, and visualized on Boards and Roadmaps.
   * - :ref:`E2.A-1.2 <scenario-a-1>`
     - Users are granted access to specific role-based functions which allow required actions and responsibilities to be assumed and executed.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | Gitlab Platform provided users and user groups alongside projects and project group permissions to ensure that projects are managed correctly.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: Gitlab Platform provides users and user group management for one or more projects through permissions that control ownership, editing, viewing, project management, and issue tracking functions.
   * - :ref:`E2.A-2.1 <scenario-a-2>`
     - Requirements are created and documented in the system.
     - Components were not available to implement in this demonstration. Requirements Management System will be included in future example implementation.
     - Components were not available to implement in this demonstration. Requirements Management System will be included in future example implementation.
   * - :ref:`E2.A-2.2 <scenario-a-2>`
     - Stakeholders receive assignments.
     - Gitlab Platform provided Epics, Issues, and Tasks to assign work to stakeholders, organized with Labels, Boards, Milestones, and Iterations.
     - | Implemented: Work is assigned to stakeholders through Epics, Issues, and Tasks, organized with Labels, tracked with Boards, Milestones, and Iterations, with notifications via email and to-do items.
   * - :ref:`E2.A-3.1 <scenario-a-3>`
     - Design solutions are documented in the Design Management System to track and maintain product materials for the software application.
     - Components were not available to implement in this demonstration. Design Management System will be included in future example implementation.
     - Components were not available to implement in this demonstration. Design Management System will be included in future example implementation.
   * - :ref:`E2.A-3.2 <scenario-a-3>`
     - Tickets are updated based on tasking.
     - Gitlab Platform provided Epics, Issues, and Tasks to document work and track tasking, organized with Labels, Boards, Milestones, and Iterations.
     - | Implemented: Work is documented through Epics, Issues, and Tasks, categorized with Labels, tracked with Boards, and scheduled against Milestones and Iterations.
   * - :ref:`E2.A-3.3 <scenario-a-3>`
     - | Product requirements and necessary changes to product vision, roadmaps, features, and grow strategy are documented accordingly to track product and component changes.
     - | Gitlab Platform provided Epics, Issues, and Tasks to document product direction, organized with Labels and Milestones and visualized on Roadmaps and Boards.
     - | Implemented: Product direction and feature changes are tracked through Epics, Issues, and Tasks, categorized with Labels and Milestones, and visualized via Roadmaps and Boards.
   * - :ref:`E2.A-4.1 <scenario-a-4>`
     - High level and technical issues are documented.
     - Gitlab Platform provided Epics, Issues, and Tasks to document high-level and technical work, organized with Labels, Boards, and Milestones.
     - Implemented: High-level and technical work is captured through Epics, Issues, and Tasks, organized with Labels, Boards, and Milestones.
   * - :ref:`E2.A-4.2 <scenario-a-4>`
     - All issues are assigned to the appropriate team member.
     - Gitlab Platform provided Issues and Tasks to assign work to team members, organized with Labels, Boards, and Milestones.
     - Implemented: Each Issue or Task is assigned to the responsible team member and organized with Labels, Boards, and Milestones.
   * - :ref:`E2.A-5.1 <scenario-a-5>`
     - Risks are identified and documented.
     - | Gitlab Platform Security Dashboard and Vulnerability Report displayed findings.

       | Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance.

     - | Implemented: Gitlab Platform provides additional risk identification and documentation tools using Compliance and Security Policy settings.

       | Implemented: Resilience Attestation Store provided product integrations and search filters to help identify products and attestations that are failing policy requirements.
   * - :ref:`E2.A-5.2 <scenario-a-5>`
     - Tickets are created and updated based on new risks. Mitigations and solutions are documented in tickets as risks are resolved.
     - | Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes; Gitlab Platform Security Dashboard and
       | Vulnerability Report displayed findings.
     - Implemented: Gitlab Platform provides additional risk identification and documentation tools using Compliance and Security Policy settings.
   * - :ref:`E2.A-6.1 <scenario-a-6>`
     - | Results of cyber intelligence and other security feeds were reviewed and documented. Tickets are created and updated to track and resolve issues related to threats.
     - | Components were not available to implement in this demonstration. Cyber Intelligence Threat and Security Metadata Feeds will be included in future example implementation.

       | Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes; Gitlab Platform Secu-rity Dashboard and Vulnerability Report displayed findings. 
     - Components were not available to implement in this demonstration. Cyber Intelligence Threat and Security Metadata Feeds will be included in future example implementation.
   * - :ref:`E2.A-6.2 <scenario-a-6>`
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - Microsoft provided demonstration of Threat Modeling Tool, threats were identified and categorized; mitigations and justifications were documented.
     - Note: This demonstration described flagged threats moving through a tool-assisted mitigation process. Justifications were documented in the tool otherwise proposed mitigations were rejected.
   * - :ref:`E2.A-6.3 <scenario-a-6>`
     - Threat Modeling System produced new model changes or presented new potential vulnerabilities.
     - Microsoft provided demonstration of Threat Modeling Tool, threats were identified and categorized; mitigations and justifications were documented.
     - Note: This demonstration described flagged threats moving through a tool-assisted mitigation process. Justifications were documented in the tool otherwise proposed mitigations were rejected.
   * - :ref:`E2.A-7.1 <scenario-a-7>`
     - Configurations are created and updated.
     - Gitlab Platform SCM provided configuration management for projects, associated systems, and software applications.
     - | Implemented: Gitlab Platform SCM provides configuration management functionality using Operate, Compliance, and Policy settings, which control build and deploy environment settings as well as operational settings for deployed assets.
   * - :ref:`E2.A-7.2 <scenario-a-7>`
     - | Tickets are created and updated as configurations change. Both Design and Requirements Management Systems are updated to track con-figuration changes over time.
     - Gitlab Platform provided Issues, Tasks, Labels, and Milestones to track configuration changes over time.
     - | Implemented: Configuration changes are tracked through Issues and Tasks, categorized with Labels and grouped under Milestones, with change history retained on each item.
   * - :ref:`E2.A-8.1 <scenario-a-8>`
     - Policies are defined and implemented in certificate, credential and secret management systems.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided policy controls of certificates and secrets management functions.

       | CyberArk Privilege Cloud and CyberArk Secrets Hub were used for management.

       | CyberArk Certificate Manager SaaS is leveraged for management of certificate and certificate policies

       | DigiCert Trust Lifecycle Manager is leveraged for management of certificate and certificate policies

       | Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance with policies governing secrets management

     - | Implemented: Microsoft Azure Entra ID was leveraged to create users and to assign roles and policies to the users. Microsoft AKV was leveraged for access and security control of certificates and secrets.

       | Note: Gitlab Platform provides credential inventory which is linked with Microsoft Azure Entra ID credentials. Microsoft Azure Entra ID provides the necessary credential management functions around policies. Gitlab Platform provides the group, project, and role assignments for Gitlab-hosted resources.

       | Implemented: Policies were applied in CyberArk Privilege Cloud and CyberArk Secrets Hub to restrict access to credentials and secrets to authorized users and service accounts.

       | Implemented: CyberArk Certificate Manager SaaS provided issuing templates, approval rules, and certificate lifecycles for deployment and management of certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided certificate profiles, base templates, and rules for deployment and management of certificates.

       | Implemented: Resilience Attestation Store provided product integrations and search filters to help identify products and attestations that are failing secrets detection scans.
   * - :ref:`E2.A-8.2 <scenario-a-8>`
     - Certificates, credentials, and secrets are scanned or tested to verify access and policy configurations.
     - | Microsoft Azure Entra ID provided assessment of credentials and role assignments. Microsoft AKV provided policy controls of certificates and secrets management functions.

       | Gitlab Platform provided users and user groups alongside projects and project group permissions to ensure that projects are managed correctly.

       | CyberArk Privilege Cloud and CyberArk Secrets Hub were used for management.

       | CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are valid and not compromised

       | DigiCert Trust Lifecycle Manager provides monitoring and scanning to verify that certificates are valid and not compromised

     - | Implemented: Microsoft Azure Entra ID was leveraged for assessing the status of users and role assignments. Microsoft AKV was leveraged for assessing the status of certificates and secrets.

       | Implemented: Gitlab Platform provides credential inventory which is linked with Microsoft Azure Entra ID credentials.

       | Note: Microsoft Azure Entra ID provides the necessary credential management functions around policies. Gitlab Platform provides the group, project, and role assignments for Gitlab-hosted resources.

       | Implemented: Policies were applied in CyberArk Privilege Cloud and CyberArk Secrets Hub and tested to verify expected outcomes.

       | Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates, certificate lifecycle status, and 47-day TLS Baseline Requirements

       | Implemented: DigiCert Trust Lifecycle Manager provided the network scan and automated alerts to identify at-risk certificates, certificate lifecycle, and automation status
   * - :ref:`E2.A-8.3 <scenario-a-8>`
     - | Certificates, credentials, and secrets are verified as safe to use and are rotated, revoked, or reissues in the event of disclosure or potential vulnerability.
     - | Microsoft Azure Entra ID provided mechanisms for the control and rotation of credentials. Microsoft AKV provided mechanisms for the revocation, rotation, and reissuance of certificates and rotation or revocation of secrets.

       | CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are not compromised.

       | DigiCert Trust Lifecycle Manager provides monitoring and scanning to verify that certificates are not compromised.

     - | Implemented: Microsoft Azure Entra ID was leveraged for assessing the status of users and role assignments. Microsoft AKV was leveraged for assessing the status of certificates and secrets.
       | Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided the network scans and automated alerts to monitor to identify at-risk certificates.
   * - :ref:`E2.A-9.1 <scenario-a-9>`
     - CI/CD Pipelines are created, updated, and maintained successfully so automated actions can be performed as required.
     - Gitlab Platform CI provided CI/CD Pipelines and pipeline editors to conduct automated actions.
     - Implemented: Gitlab CI provides automation processes and tools to build and manage CI/CD automation.
   * - :ref:`E2.A-9.2 <scenario-a-9>`
     - Configurations, IaC, and source code are obtained by CI/CD Pipelines and are used as part of the build process.
     - | Gitlab Platform Runners automated CI/CD activities on source code, IaC, and configurations. Gitlab Platform SCM provided source control for all source code, IaC, and configurations.
     - Implemented: Gitlab Runners provides CI/CD automation for source code, IaC, and configurations hosted in Gitlab SCM-managed projects.
   * - :ref:`E2.A-9.3 <scenario-a-9>`
     - Requirements verified and logged by CI/CD Pipelines.
     - Gitlab Platform Runners automated CI/CD activities on source code, IaC, and configurations.
     - Implemented: Gitlab Runners provide CI/CD automation which logs all automated activities.
   * - :ref:`E2.A-10.1 <scenario-a-10>`
     - User access to systems (e.g., Ticketing and Design Management System) is allowed or denied based on ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | Gitlab provided access to a suite of planning tools and capabilities and granted access to Entra ID users via SSO.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: Roles and Permissions were defined within Gitlab, restricting user access within Gitlab to the policy definitions.
   * - :ref:`E2.A-10.2 <scenario-a-10>`
     - Requirement and design documents are protected and stored. Only authorized personnel can access and distribute them.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | Gitlab provided access to a suite of planning tools and capabilities and granted access to Entra ID users via SSO.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: Roles and Permissions were defined within Gitlab, restricting user access within Gitlab to the policy definitions.
   * - :ref:`E2.A-10.3 <scenario-a-10>`
     - | Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices, including rotation and short expiration times.
     - | Microsoft Entra ID provided token-based authentication via managed identities and workload identity federation. 
       | NextLabs was supported by API-based authentication. 
     - | Partially Implemented: Machine/workload identities were implemented to provide machine or service-level authentication using short-lived tokens. Certificate-based authentication and lifecycle management controls will be included in a future Example Implementation.
       | Partially Implemented: API-based authentication was implemented to support NextLabs CloudAZ, SkyDRM, and GitLab Enforcer. Machine identity with certificate-based authentication and lifecycle management controls will be included in a future Example Implementation. 
   * - :ref:`E2.A-11.1 <scenario-a-11>`
     - New work items, tickets, or issues are generated.
     - | Gitlab Duo provided analysis of requirements captured in Gitlab Issues and created new Work Items and Issues.

       | Sagittal Neo provided analysis of requirements captured in Gitlab Issues and created new Work Items and Issues.

     - | Implemented: Gitlab Duo and Flow Planner agent provides automated analysis of existing context in Gitlab Issues, source code, and merge requests and generates new issues to track status of requirements.

       | Implemented: Sagittal Neo provides automated analysis of existing context in Gitlab Issues, source code, and merge requests and generates new issues to track status of requirements.
   * - :ref:`E2.A-11.2 <scenario-a-11>`
     - Existing work items, tickets, or issues are assigned to epics or user stories.
     - | Gitlab Duo provided analysis and curation of existing Work Items and Issues in Gitlab Issues and assigns work to users accordingly.

       | Sagittal Neo provided analysis and curation of existing Work Items and Issues in Gitlab Issues and assigns work to users accordingly.

     - | Implemented: Gitlab Duo provides automated analysis of existing context in Gitlab Issues and assigned Work Items or Issues to users.

       | Implemented: Sagittal Neo provides automated analysis of existing context in Gitlab Issues and assigned Work Items or Issues to users. Note: Sagittal Neo integration of Gitlab Issues is beta and assignment of Issues to Parents, Milestones, or Work Items is currently unsupported.
   * - :ref:`E2.A-11.3 <scenario-a-11>`
     - Duplicate work items, tickets, or issues are marked as closed or removed.
     - | Gitlab Duo provided automated closing of duplicate or deprecated Work Items or Issues.

       | Sagittal Neo provided automated closing of duplicate or deprecated Work Items or Issues.

     - | Implemented: Gitlab Duo provides automated closing of Work Items or Issues that were deemed closed, duplicated, or deprecated.

       | Implemented: Sagittal Neo provides automated closing of Work Items or Issues that were deemed closed, duplicated, or deprecated.
   * - :ref:`E2.A-11.4 <scenario-a-11>`
     - Standards or framework compliance requirements are documented for project, requirements, or risk management systems.
     - | Gitlab Duo provided analysis of standards and frameworks provided as context.

       | Sagittal Neo provided analysis of standards and frameworks provided as context.

     - | Implemented: Gitlab Duo provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.

       | Implemented: Sagittal Neo provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.
   * - :ref:`E2.A-11.5 <scenario-a-11>`
     - Summaries are documented in project or requirements management system.
     - | Gitlab Duo provided summarization of project and task requirements in Work Items and Issues.

       | Sagittal Neo and Semantic Linter provided summarization of project and task requirements in Work Items and Issues.

     - | Implemented: Gitlab Duo provides generated documentation and requirements based on context included in Work Items, Issues, and Merge Requests.

       | Implemented: Sagittal Neo and Semantic Linter provide generated documentation and requirements based on context included in Work Items, Issues, and Merge Requests.
   * - :ref:`E2.A-11.6 <scenario-a-11>`
     - Required resources are identified, documented for project or design management systems.
     - | Gitlab Duo identified specific resources (e.g., source code, functions, software dependencies) required by project-specific Work Items or Issues.

       | Sagittal Neo and Semantic Linter identified specific resources (e.g., source code, functions, software dependencies) required by project-specific Work Items or Issues.

     - | Implemented: Gitlab Duo provides specific source code changes, functions, or software dependencies associated with project-specific Work Items, Issues, or Merge Requests.

       | Implemented: Sagittal Neo and Semantic Linter provide specific source code changes, functions, or software dependencies associated with project-specific Work Items, Issues, or Merge Requests.
   * - :ref:`E2.A-11.7 <scenario-a-11>`
     - Modifications are generated and saved for future use.
     - | Gitlab Duo provided analysis of requirements captured in Gitlab Issues and created new Work Items and Issues.

       | Sagittal Neo provided analysis of requirements captured in Gitlab Issues and created new Work Items and Issues.

     - | Implemented: Gitlab Duo provides automated analysis of existing context in Gitlab Issues, source code, and merge requests and generates new issues to track status of requirements.

       | Implemented: Sagittal Neo provides automated analysis of existing context in Gitlab Issues, source code, and merge requests and generates new issues to track status of requirements.
   * - :ref:`E2.A-11.8 <scenario-a-11>`
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - | Gitlab Duo provided analysis of risks and vulnerabilities provided as context from Gitlab Security Dashboard and Vulnerability Report.

       | Sagittal Neo provided analysis of risks and vulnerabilities provided as context from Gitlab Security Dashboard and Vulnerability Report.

     - | Implemented: Gitlab Duo provides generated content based on associated security requirements included in Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.

       | Implemented: Sagittal Neo provides generated content based on associated security requirements included in Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.
   * - :ref:`E2.A-11.9 <scenario-a-11>`
     - Users, service accounts, or other principals are identified in credential or secrets management system.
     - | Gitlab Duo provided checklist items, Work Items, and Issues that identify the existence of detected secrets.

       | Sagittal Neo provided checklist items, Work Items, and Issues that identify the existence of detected secrets.

     - | Implemented: Gitlab Duo provides generated content based on detected secrets documented in Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.

       | Implemented: Sagittal Neo provides generated content based on detected secrets documented in Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.

.. _e2-develop-results:

E2 Develop Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.B-1.1 <scenario-b-1>`
     - Source code, unit tests, and automation scripts are created.
     - | Gitlab Platform Web UI provided an IDE interface for development of source code, unit tests, and automation scripts. Gitlab Platform SCM provided source control for all source code, unit tests, and automation scripts

       | Microsoft Visual Studio Code provided IDE interface for development of source code, unit tests, and automation scripts.

     - | Implemented: Gitlab Web UI provides IDE interface for development of source code, unit tests, and automation scripts hosted in Gitlab SCM-managed projects

       | Implemented: Microsoft Visual Studio Code was leveraged for development source code, unit tests, and automation scripts.
   * - :ref:`E2.B-1.2 <scenario-b-1>`
     - Artifacts are retrieved and managed via a repository.
     - Gitlab Platform Container and Package Registry features provided storage for artifacts built by CI/CD Pipelines.
     - | Implemented: Gitlab Container and Package Registries provide build automation with a location to storage generated artifacts such as containers or software libraries.
   * - :ref:`E2.B-1.3 <scenario-b-1>`
     - Code is built and unit tests are run.
     - | Gitlab Platform SCM provided source control for all source code and unit tests. Gitlab Web UI provided development tools necessary for creating source code and unit test.
     - | Implemented: Gitlab SCM provides source control for all source code and unit tests. Gitlab Web UI provides IDE and editor functionality to create source code and unit test.
   * - :ref:`E2.B-2.1 <scenario-b-2>`
     - Any vulnerabilities are found, and logs are provided.
     - | GitLab Platform CI and Runners executed Gitlab Advanced SAST. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform
       | Security Dashboard and Vulnerability Report.

       | Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance.

     - | Implemented: Gitlab Advanced SAST identifies vulnerabilities in application source code. GitLab Runners and Gitlab CI pipeline automation capture vulnerability findings and metadata in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: Resilience Attestation Store provided product integrations and search filters to help identify products and attestations that are failing policy requirements. Note: Resilience Platform provides automated operation of SAST components. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.B-2.2 <scenario-b-2>`
     - Security issues and style problems are found via the linting tool. Logs are provided to the developer.
     - | Gitlab Platform Runners automated project linting checks and logged findings. Gitlab CI captured lint findings in Code Quality Reports.

       | Resilience Valint CLI provided evidence collection of automated linting actions

     - | Implemented: Gitlab Runners provided project linting checks and captured code quality issues which are recorded in Gitlab CI Code Quality Reports.

       | Implemented: Resilience Valint collects results from automated linting components and logs compliance status.
   * - :ref:`E2.B-2.3 <scenario-b-2>`
     - SCA tool runs, vulnerabilities are detected, and logs are provided.
     - | Gitlab Platform CI and Runners executed Gitlab Dependency Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Resilience Valint CLI provided evidence collection of automated SCA actions

     - | Implemented: Gitlab Dependency Scanning identifies vulnerabilities in application dependencies, including transitive dependencies. GitLab Runners and Gitlab CI pipeline automation capture vulnerability findings and metadata in the project’s Security tab, merge request widget, and dependency inventory in the Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: Resilience Valint collects results from automated SCA components and logs compliance status.
   * - :ref:`E2.B-2.4 <scenario-b-2>`
     - Credentials, Keys, and other sensitive information are detected. Results are provided to developers.
     - | Gitlab Platform CI and Runners executed Gitlab Secret Detection. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Resilience Valint CLI provided evidence collection of automated secret detection scanning actions

     - | Implemented: Gitlab Secret Detection identifies exposed credentials, keys, and sensitive information across three layers: push protections block secrets before commits reach the repository, pipeline-level scanning prevents plaintext secrets from use during jobs, and Git history analysis to find previously removed secrets still being tracked. GitLab Runners and Gitlab CI pipeline automation capture vulnerability findings and metadata in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: Resilience Valint collects results from automated secret detection components and logs compliance status. Note: Resilience Platform provides automated operation of secrets scanning components. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.B-3.1 <scenario-b-3>`
     - IaC scripts are created.
     - | Gitlab Platform Web UI provided an IDE interface for development of IaC scripts. Gitlab Platform SCM provided source control for all IaC scripts

       | Microsoft Visual Studio Code provided IDE interface for development of IaC scripts.

     - | Implemented: Gitlab Web UI provides IDE interface for development of IaC scripts hosted in Gitlab SCM-managed projects.

       | Implemented: Microsoft Visual Studio Code was leveraged for development of IaC scripts.
   * - :ref:`E2.B-3.2 <scenario-b-3>`
     - IaC code problems are found and logs provided.
     - | Gitlab Platform CI and Runners executed Gitlab IaC Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Resilience Valint CLI provided evidence collection of automated IaC scanning actions.

     - | Implemented: Gitlab IaC Scanning identifies security and compliance issues in infrastructure-as-code. GitLab Runners and Gitlab CI pipeline automation capture vulnerability with full scan output in CI job logs. These findings are also shown in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: Resilience Valint collects output from automated IaC components and logs compliance status.

       | Note: Resilience Platform provides automated operation of code quality components. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.B-4.1 <scenario-b-4>`
     - Changes are reviewed by approved developers prior to merging.
     - Gitlab Platform SCM provided branching, tagging and merge request functionality for all hosted projects.
     - Implemented: Gitlab SCM provides branching and merge requests for code changes and tagging functionality for individual commits or releases.
   * - :ref:`E2.B-4.2 <scenario-b-4>`
     - Code is created by developers and committed to source code repositories.
     - Gitlab Platform SCM provided commit functionality, branching, tagging and merge request functionality for all hosted projects.
     - Implemented: Gitlab SCM provides capabilities to commit, branch, tag and merge code changes.
   * - :ref:`E2.B-4.3 <scenario-b-4>`
     - Code is scanned and is not committed if errors are found.
     - | Gitlab Platform SCM provided source control for all source code. Gitlab Platform Security Dashboard and Vulnerability Report captured detected secrets,
       | SAST, and SCA findings.
     - | Implemented: Gitlab Security Dashboard and Vulnerability Report capture findings detected by secret scanning, SCA, and SAST components in Gitlab-hosted projects.
   * - :ref:`E2.B-4.4 <scenario-b-4>`
     - Code that has not been approved cannot be merged into main.
     - Gitlab Platform SCM provided branch defaults, protected branches, merge rules, push rules, and security policies to enforce compliance.
     - | Implemented: Gitlab SCM provides branching, pushing, and merging protections via group, project, or repository-level branch defaults, protected branches, merge rules, and security policies.
   * - :ref:`E2.B-5.1 <scenario-b-5>`
     - Credentials are stored and managed securely.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments.
       | CyberArk Privilege Cloud and CyberArk Secrets Hub stored credentials and provided secure access during the Develop phase.

       | Gitlab Platform provided users and user groups alongside projects and project group permissions to ensure that projects are managed correctly.

     - | Implemented: Microsoft Azure Entra ID is leveraged to manage credentials.

       | Implemented: CyberArk Privilege Cloud and Secrets Hub securely stores service account and API credentials. These credentials are provided to authorized requestors.

       | Implemented: Gitlab Platform provides users and user group management for one or more projects through permissions that control ownership, editing, viewing, CI/CD automation, project management, and issue tracking functions.
   * - :ref:`E2.B-5.2 <scenario-b-5>`
     - Keys and other secrets are stored and managed securely.
     - | Microsoft AKV provided storage and management functions for secrets.

       | CyberArk Privilege Cloud and CyberArk Secrets Hub stored keys and provided secure access during the Develop phase.

     - | Implemented: Microsoft AKV is leveraged to manage secrets.

       | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.
   * - :ref:`E2.B-5.3 <scenario-b-5>`
     - Certificates are stored and managed (e.g., issuance, rotation, revocation) securely.
     - | Microsoft AKV provided storage and management functions for certificates.

       | CyberArk Machine Identity Security generated and stored signing material, and provided secure access during the Develop phase. CyberArk Certificate Manager SaaS is leveraged for management and distribution of certificates.

       | DigiCert Trust Lifecycle Manager provided management for public and private certificate authorities and stored signed certificates.

     - | Implemented: Microsoft AKV is leveraged to manage certificates. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in
       | Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored and provided to authorized requestors. CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates, certificate lifecycle status, and 47-day TLS Baseline Requirements.

       | Implemented: DigiCert Trust Lifecycle Manager stores and maintains publicly-verified TLS certificates.
   * - :ref:`E2.B-6.1 <scenario-b-6>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.B-6.2 <scenario-b-6>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.B-6.3 <scenario-b-6>`
     - Logs of firmware updates or changes are captured
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.B-7.1 <scenario-b-7>`
     - Software components are digitally signed, and secrets are stored and protected by HSM.
     - | Microsoft AKV provided signing and management controls for certificates.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use during the Develop phase.

       | Resilience’s Valint tool is used to sign software components. Resilience’s Attestation Store securely stores signatures and related artifacts.

     - | Implemented: Microsoft AKV is leveraged to manage certificates used to sign software components. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored and provided to authorized requestors.

       | Implemented: Resilience Valint generates signatures using signing material provided by CyberArk Machine Identity Security. These signatures are securely stored in the Resilience Attestation Store. Note: Resilience Platform provides continuous validation of signed material. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.B-7.2 <scenario-b-7>`
     - Signed software components are authentic and not tampered with.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use during the Develop phase.

       | CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are valid and not compromised.

       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates, certificate lifecycle status, and 47-day TLS Baseline Requirements.

       | Implemented: Resilience Valint validates signatures using signing material provided by CyberArk Machine Identity Security. These generated artifacts are securely stored in the Resilience Attestation Store. Note: Resilience Platform provides continuous verification of authenticity of signed material. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.B-7.3 <scenario-b-7>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.B-8.1 <scenario-b-8>`
     - Certificates and private keys are stored and managed securely in the Certificate Management System.
     - | Microsoft AKV provided storage and management functions for certificates.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use during the Develop phase.

       | CyberArk Certificate Manager SaaS is leveraged for management and distribution of certificates.

       | DigiCert Trust Lifecycle Manager is leveraged for management and distribution of certificates

     - | Implemented: Microsoft AKV is leveraged to manage certificates. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager manages certificates generated for code signing purposes. These code signing certificates are securely stored and provided to authorized requestors. Private keys are accessed via secure interfaces.

       | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, managed, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided certificates, API keys, and service connections to securely access, manage, and store certificates.
   * - :ref:`E2.B-8.2 <scenario-b-8>`
     - Secrets and credentials are securely managed and stored in Secrets Management System.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided storage and management functions for secrets.
       | CyberArk Privilege Cloud and CyberArk Secrets Hub stored credentials and provided secure access during the Develop phase.

     - | Implemented: Microsoft Azure Entra ID was leveraged to manage service accounts and service principals. Microsoft AKV was leveraged to manage secrets.

       | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.
   * - :ref:`E2.B-9.1 <scenario-b-9>`
     - Scripts to automate the CI/CD pipelines and build its environments are stored in SCM.
     - | Gitlab Platform SCM feature provided source control for all CI/CD Pipelines build scripts.

       | Microsoft Visual Studio Code provided IDE functionality to maintain source control for all CI/CD Pipelines build scripts.

     - | Implemented: Gitlab SCM provides source control for all CI/CD Pipeline build scripts.

       | Implemented: Microsoft Visual Studio Code was leveraged for implementation of all CI/CD Pipeline build scripts.
   * - :ref:`E2.B-10.1 <scenario-b-10>`
     - Only authorized users can access and perform actions on source code management systems.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | NextLabs’ SkyDRM and Windows Enforcer components were used to restrict actions to authorized users on developer workstations. NextLabs’ Gitlab Enforcer was used to restrict actions on Gitlab.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and enforced on source code management systems through the SkyDRM, Windows Enforcer, and Gitlab Enforcer Components.
   * - :ref:`E2.B-10.2 <scenario-b-10>`
     - Only authorized endpoints can access source control systems and development systems.
     - NextLabs’ SkyDRM and CloudAz components were used to restrict repository usage to authorized developer workstations.
     - Implemented: ZT policy was written and defined within NextLabs’ CloudAz and enforced on endpoints through the SkyDRM and Windows Enforcer components.
   * - :ref:`E2.B-10.3 <scenario-b-10>`
     - Authorized users can make changes to restricted branches.
     - | NextLabs’ SkyDRM, CloudAz, and Gitlab enforcer components prevented unauthorized users from making change to restricted branches both on development workstations and within Gitlab.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and changes to branches were restricted to authorized users through the SkyDRM, Windows Enforcer, and Gitlab Enforcer Components.
   * - :ref:`E2.B-10.4 <scenario-b-10>`
     - | Strong machine identity is established using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices,
       | including rotation and short expiration times.
     - | Microsoft Entra ID provided token-based authentication via managed identities and workload identity federation.
       | NextLabs was sup-ported by API-based authentication. 
     - | Partially Implemented: Machine/workload identities were implemented to provide machine or service-level authentication using short-lived tokens. Certificate-based authentication and lifecycle management controls will be included in a future Example Implementation.
       | Partially Implemented: API-based authentication was implemented to support NextLabs CloudAZ, SkyDRM, and GitLab Enforcer. Machine identity with certificate-based authentication and lifecycle management controls will be included in a future Example Implementation.
   * - :ref:`E2.B-10.5 <scenario-b-10>`
     - Only pipeline runs satisfying the applicable ZT policy conditions are permitted to advance.
     - NextLabs’ CloudAz and Gitlab Enforcer components implemented a ZT policy gate within Gitlab pipelines to enforce ZT policies within each pipeline.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and enforced by the Gitlab Enforcer. Pipeline runs were required to comply with ZT policies (including proper tags, secure IP ranges, and low-risk profiles) before being allowed to proceed.
   * - :ref:`E2.B-11.1 <scenario-b-11>`
     - Source code and configuration files are generated and changes, explanations, and commits are captured.
     - | Gitlab Duo generated source code, configuration, and documentation changes are contextually tracked in Gitlab Issues, Boards and Milestones.

       | Sagittal Neo generated source code, configuration, and documentation changes are contextually tracked in Gitlab Issues, Boards and Milestones.

     - | Implemented: Gitlab Duo provides generated user story and requirements based on changes to source code, configuration files, and project documentation
       | associated with Gitlab source code repositories. Gitlab Duo organized generated user story and requirements content based on Labels and Milestones.

       | Implemented: Sagittal Neo provides generated user story and requirements based on changes to source code, configuration files, and project documentation
       | associated with Gitlab source code repositories. Sagittal Neo organized generated user story and requirements based on Gitlab Labels. Note: Note:
       | Sagittal Neo integration of Gitlab Issues is beta and assignment of Issues to Parents, Milestones, or Work Items is currently unsupported.
   * - :ref:`E2.B-11.2 <scenario-b-11>`
     - Source code and configuration files are updated with generated changes and documented explanations.
     - | Gitlab Duo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

       | Sagittal Neo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

     - | Implemented: Gitlab Duo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.
   * - :ref:`E2.B-11.3 <scenario-b-11>`
     - Code and configurations are brought into compliance with specified standards.
     - | Gitlab Duo provided code and configuration changes based on security and other compliance requirements.

       | Sagittal Neo provided code and configuration changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo provides code and configuration changes based on security reports that provide findings and proposed remediations.

       | Implemented: Sagittal Neo provides code and configuration changes based on security reports that provide findings and proposed remediations.
   * - :ref:`E2.B-11.4 <scenario-b-11>`
     - Vulnerabilities are remediated through refactored code and committed to SCM.
     - | Gitlab Duo generated code and configuration changes based on security and other compliance requirements.

       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo provides code and configuration changes based on detected security findings that require remediation.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings that require remediation.
   * - :ref:`E2.B-11.5 <scenario-b-11>`
     - Dependency lists are optimized to remove or replace vulnerable libraries and updates are reflected in SCM or artifact repositories.
     - | Gitlab Duo provided code and configuration changes based on security and other compliance requirements.

       | Sagittal Neo provided code and configuration changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo provides code and configuration changes based on detected security findings or provided reports that require remediation.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings or provides reports that require remediation.
   * - :ref:`E2.B-11.6 <scenario-b-11>`
     - Source code and source control artifacts are updated with generated commits, branches, and pull requests.
     - | Gitlab Duo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

       | Sagittal Neo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

     - | Implemented: Gitlab Duo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.
   * - :ref:`E2.B-11.7 <scenario-b-11>`
     - License compliance is provided and includes steps to replace non-compliant dependencies with acceptable alternatives.
     - | Gitlab Duo provided software dependency changes based on security and other compliance requirements.

       | Sagittal Neo provided software dependency changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo recommends changing dependencies based on licensing and security reports that provide findings and proposed remediations.

       | Implemented: Sagittal Neo recommends changing dependencies based on licensing and security reports that provide findings and proposed remediations.
   * - :ref:`E2.B-11.8 <scenario-b-11>`
     - | Exposed secrets are identified and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or credentials.
     - | Gitlab Duo generated code and configuration changes based on security and other compliance requirements.

       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo provides code and configuration changes based on detected security findings that require remediation.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings that require remediation.
   * - :ref:`E2.B-11.9 <scenario-b-11>`
     - Plans are generated and provide methods to mitigate or remediate vulnerabilities found in artifacts.
     - | Gitlab Duo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

       | Sagittal Neo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

     - | Implemented: Gitlab Duo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

.. _e2-build-results:

E2 Build Phase
^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.C-1.1 <scenario-c-1>`
     - CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed.
     - Gitlab Platform CI provided CI/CD Pipelines for conducting automated build activities
     - Implemented: Gitlab CI provides automation processes and tools for build activities.
   * - :ref:`E2.C-1.2 <scenario-c-1>`
     - Configurations, IaC, and source code are obtained by CI/CD pipelines and are used as part of the build process.
     - | Gitlab Platform Runners automated CI/CD activities on source code, IaC, and configurations. Gitlab Platform SCM provided source control for all source code, IaC, and configurations
     - Implemented: Gitlab Runners provides CI/CD automation for source code, IaC, and configurations hosted in Gitlab SCM-managed projects.
   * - :ref:`E2.C-1.3 <scenario-c-1>`
     - CI/CD Pipelines run all build process components, and each component generates output for tracking status and logging de-tailed information.
     - | Gitlab Platform Runners automated CI/CD activities on source code, IaC, and configurations. Gitlab Platform SCM provided source control for all source code, IaC, and configurations.
     - Implemented: Gitlab Runners provides CI/CD automation for source code, IaC, and configurations hosted in Gitlab SCM-managed projects.
   * - :ref:`E2.C-1.4 <scenario-c-1>`
     - | Output that was logged by the CI/CD Pipelines are returned to SCM and Configuration Management Systems to track status and detailed information about the build process.
     - Gitlab Platform Runners automated logging of build activities.
     - Implemented: Gitlab Runners provides logging automation for Gitlab SCM-managed projects.
   * - :ref:`E2.C-1.5 <scenario-c-1>`
     - Components and artifacts either deployed, managed, or used by the build process are leveraging approved configurations.
     - Components were demonstrated in Example Implementation 1.
     - Components were demonstrated in Example Implementation 1.
   * - :ref:`E2.C-1.6 <scenario-c-1>`
     - Components and artifacts that have been updated in the build are added to the configuration management system.
     - Components were demonstrated in Example Implementation 1.
     - Components were demonstrated in Example Implementation 1.
   * - :ref:`E2.C-2.1 <scenario-c-2>`
     - The build environment is isolated from host systems or other environments and is automated.
     - Gitlab Platform Environments provided separate configurations for maintaining isolated build environments.
     - Implemented: Gitlab Environments are defined for build environments to maintain isolation and parallel configurations.
   * - :ref:`E2.C-2.2 <scenario-c-2>`
     - The CI/CD pipeline used CLI tools and binaries and accessed libraries within the isolated environment.
     - Gitlab Platform Runners provided build actions that automate the use of CLI tools, binaries, and other software dependencies.
     - Implemented: Gitlab Runners execute CLI, binaries, and other dependencies to perform build activities.
   * - :ref:`E2.C-2.3 <scenario-c-2>`
     - Artifacts are created and stored in the artifact repository.
     - Gitlab Platform Container and Package Registry features provided storage for artifacts built by CI/CD Pipelines.
     - | Implemented: Gitlab Container and Package Registries provide build automation with a location to storage generated artifacts such as containers or software libraries.
   * - :ref:`E2.C-3.1 <scenario-c-3>`
     - IaC Scanner identifies security vulnerabilities and compliance issues before IaC is executed.
     - | Gitlab Platform Runners automated IaC scanning actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured IaC findings.
     - | Implemented: Gitlab Runners provides IaC scanning actions that generate vulnerability logs which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.C-3.2 <scenario-c-3>`
     - Issues are created and resolved, and logs of changes are maintained.
     - Gitlab Platform provided Issues and Tasks to track remediation work and document changes, organized with Labels, Boards, and Milestones.
     - Implemented: GitLab Issues and Tasks organize items with Labels, Boards and Milestones while capturing full change histories of each work item.
   * - :ref:`E2.C-3.3 <scenario-c-3>`
     - Build environment is provisioned and managed based on scanned IaC artifacts to ensure consistency.
     - Gitlab Platform CI provided linked CI/CD Pipelines that can automatically deploy environment updates
     - Implemented: Gitlab CI provides automated deployment of default branches or specific environments based on approved and merged IaC changes
   * - :ref:`E2.C-4.1 <scenario-c-4>`
     - Vulnerabilities, compliance issues, and security risks from software libraries are identified.
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings.
     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.

       | Note: Resilience Platform provides data collection, analysis and reporting of vulnerabilities identified by Resilience Valint when used for evidence collection. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.C-4.2 <scenario-c-4>`
     - Software library artifacts used as part of the build are stored in the artifact repository.
     - Gitlab Platform Container and Package Registry features provided storage for artifacts built by CI/CD Pipelines.
     - | Implemented: Gitlab Container and Package Registries provide build automation with a location to storage generated artifacts such as containers or software libraries.
   * - :ref:`E2.C-5.1 <scenario-c-5>`
     - Unit tests are pulled from SCM and run successfully against known functional criteria.
     - Gitlab Platform Runners automated project unit testing actions and logged findings. Gitlab CI captured unit test findings in Unit Test Reports.
     - Implemented: Gitlab Runners provided automated project unit testing and captured findings which are recorded in Gitlab CI Unit Test Reports.
   * - :ref:`E2.C-5.2 <scenario-c-5>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results including issues (e.g., defects) in the ticketing system.
     - | Gitlab Platform CI provided CI/CD Pipelines for conducting automated build activities. Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab CI captures output from automated build activities and provides integrations with Gitlab Issues to generate new issues from completed build jobs.
   * - :ref:`E2.C-6.1 <scenario-c-6>`
     - | CI/CD Pipelines are provisioned in the build environment successfully and automated actions can be performed for security SAST, SCA, IaC Scanner, Secrets Scanner, and linting tools.
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings. Gitlab Platform Runners automated project linting checks and logged findings. Gitlab CI captured lint findings in Code Quality Reports.

       | Resilience Valint CLI provided evidence collection of automated SCA, SAST, and linting actions.

     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report. Gitlab Runners provided project linting checks and captured code quality issues which are recorded in Gitlab CI Code Quality Reports.

       | Implemented: Resilience Valint collects results from automated SCA, SAST, and linting components then logs compliance status. Note: Resilience Platform provides automated operation of security scanning components. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.C-6.2 <scenario-c-6>`
     - Code is created and each security tool generates results.
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings.

       | Resilience Valint CLI provided evidence collection of automated scanning and testing actions.

     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: Resilience Valint collects results from automated scanning and testing components then logs compliance status. Note: Resilience Platform provides data collection, analysis and reporting of vulnerabilities identified by Resilience Valint when used for evidence collection. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.C-6.3 <scenario-c-6>`
     - Security tools provide outputs of issues via notifications or logs to stakeholders.
     - | Gitlab Platform Security Dashboard and Vulnerability Report captured security findings.

       | Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance.

     - | Implemented: Gitlab Platform integrates with collaborative tools such as email and direct messaging for sending notifications.

       | Implemented: Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance. Note: Resilience Platform provides data collection, analysis and reporting of vulnerabilities identified by Resilience Valint when used for evidence collection. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.C-7.1 <scenario-c-7>`
     - Sensitive information was securely retrieved during the build process.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided storage and management functions for certificates and secrets.

       | CyberArk Certificate Manager SaaS is leveraged for access and distribution of certificates.

       | DigiCert Trust Lifecycle Manager is leveraged for access and distribution of certificates.

     - | Implemented: Microsoft Azure Entra ID is leveraged to manage credentials. Microsoft AKV is leveraged to manage certificates and secrets. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, managed, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided API keys and service connections to securely access stored certificates.
   * - :ref:`E2.C-7.2 <scenario-c-7>`
     - Sensitive information is protected by various management systems and HSMs to prevent unauthorized access and disclosure.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided storage and management functions for certificates and secrets.

       | CyberArk Privilege Cloud and CyberArk Secrets Hub stored credentials and provided secure access.

       | CyberArk Machine Identity Security stores code signing certificates within an HSM.

     - | Implemented: Microsoft Azure Entra ID is leveraged to manage credentials. Microsoft AKV is leveraged to manage certificates and secrets. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.
   * - :ref:`E2.C-7.3 <scenario-c-7>`
     - The Build phase environment has authorized access to sensitive information with proper credentials and configuration.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided storage and management functions for certificates and secrets.

       | CyberArk Privilege Cloud and CyberArk Secrets Hub provided secure access to sensitive secrets.

       | CyberArk Certificate Manager SaaS is leveraged for access and distribution of certificates.

       | DigiCert Trust Lifecycle Manager is leveraged for access and distribution of certificates.

     - | Implemented: Microsoft Azure Entra ID is leveraged to manage credentials. Microsoft AKV is leveraged to manage certificates and secrets.

       | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.

       | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, managed, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided API keys and service connections to securely access stored certificates.
   * - :ref:`E2.C-7.4 <scenario-c-7>`
     - The HSM is tamper-resistant in maintaining digital assets (e.g., private keys and certificates).
     - | Microsoft AKV provided storage and management functions for certificates.

       | CyberArk Machine Identity Security stores code signing certificates within a tamper-resistant HSM.

     - | Implemented: Microsoft AKV is leveraged to manage certificates. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.
   * - :ref:`E2.C-8.1 <scenario-c-8>`
     - Source code or configuration credentials that are exposed are detected prior to the build.
     - | Gitlab Platform Runners provided automated secret detection.

       | NextLabs’ CloudAz and Gitlab Enforcer components scan and verify that unapproved credentials are detected, blocking build progress until the issue is resolved.

     - | Implemented: Gitlab Runners provides secret detection that generated vulnerability logs which prevents leaked or exposed secrets from being used in CI/CD Pipelines.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz to verify that source code and configuration credentials are scanned for exposures. The Gitlab Enforcer blocks build pipelines from progressing if unapproved credentials are detected.
   * - :ref:`E2.C-8.2 <scenario-c-8>`
     - Findings are logged by SCA and stakeholders are notified.
     - | Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Runners provided automated secret detection.
       | Gitlab Platform Security Dashboard and Vulnerability Report captured SCA and secret detection findings.
     - | Implemented: Gitlab Runners provides Gitlab SCA dependency scanning and secret detection actions that generated vulnerability logs which are recorded in
       | Gitlab Platform Security Dashboard and Vulnerability Report. Gitlab Runners provides secret detection that generated vulnerability logs which prevents leaked or exposed secrets from being used in CI/CD Pipelines.
   * - :ref:`E2.C-9.1 <scenario-c-9>`
     - Software packages (e.g., artifacts and dependencies) are securely stored and managed in the artifact repository.
     - Gitlab Platform Container and Package Registry features provided storage for artifacts built by CI/CD Pipelines.
     - | Implemented: Gitlab Container and Package Registries provide build automation with a location to storage generated artifacts such as containers or software libraries.
   * - :ref:`E2.C-9.2 <scenario-c-9>`
     - Information is logged by each tool for auditing of the build status.
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings. Gitlab Platform Runners automated project linting checks and logged findings. Gitlab CI captured lint findings in Code Quality Reports.
     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report. Gitlab Runners provided project linting checks and captured code quality issues which are recorded in Gitlab CI Code Quality Reports.
   * - :ref:`E2.C-10.1 <scenario-c-10>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.C-10.2 <scenario-c-10>`
     - Logs of firmware updates or changes are captured
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.C-11.1 <scenario-c-11>`
     - Software components are digitally signed and secrets are stored and protected by HSM.
     - | Microsoft AKV provided signing and management controls for certificates.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to sign software components. Resilience’s Attestation Store securely stores signatures and related artifacts.

       | Gitlab Platform CI automated signing jobs generated and verified container images.

     - | Implemented: Microsoft AKV is leveraged to manage certificates used to sign software components. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies signatures using signing material provided by CyberArk Machine Identity Security. These signatures are securely stored in the Resilience Attestation Store.

       | Implemented: Gitlab CI uses job templates to integrate sigstore/cosign keyless signing of generated container image. These automated signing jobs use Gitlab OIDC-issued identity to sign images with immutable digests. GitLab CI pipelines provide verification steps to ensure successful image signing.
   * - :ref:`E2.C-11.2 <scenario-c-11>`
     - Signed software components are authentic and not tampered with.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are valid and not compromised.

       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates, certificate lifecycle status, and 47-day TLS Baseline Requirements.

       | Implemented: Resilience Valint generates and verifies signatures using signing material provided by CyberArk Machine Identity Security. These signatures are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.C-11.3 <scenario-c-11>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.C-12.1 <scenario-c-12>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - | Gitlab Platform CI and Runners executed Gitlab Container Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to generate SLSA provenance records. Resilience’s Attestation Store securely stores SLSA artifacts.

     - | Implemented: Gitlab Container Scanning identifies known vulnerabilities in the packages and dependencies in container images. GitLab Runners and Gitlab CI pipeline automation capture vulnerability with full scan output in CI job logs. These findings are also shown in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SLSA provenance records (e.g., SLSA attestation) using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.C-12.2 <scenario-c-12>`
     - Logs of results are available for tracking the provenance of generated artifacts.
     - | Gitlab CI provided CI/CD Pipelines to capture evidence and to associate evidence with Gitlab Release artifacts.

       | Resilience’s Valint tool generated logs for attestation and verification of any SLSA artifacts. Resilience’s Attestation Store securely stored attestation and verification log output related to any SLSA artifacts.

     - | Implemented: Gitlab CI captures supply chain evidence and attaches it to artifacts hosted as Gitlab Releases.

       | Implemented: Resilience Valint generates logs that capture the attestation or verification statuses for SLSA artifacts. Any log output is securely stored in the Resilience Attestation Store. Note: Resilience Platform provides continuous validation of SLSA artifacts. Resilience Platform was not implemented as part of this demonstration.
   * - :ref:`E2.C-13.1 <scenario-c-13>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | CyberArk Machine Identity Security provided code signing certificates to support SBOM signing. Signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to generate and sign SBOMs related to software components. Resilience’s Attestation Store securely stores related artifacts.

       | Gitlab Platform CI and Runners executed Gitlab Dependency Scanning. Generated dependency inventories are aggregated in the Gitlab Dependency List. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report. GitLab Platform Package Registry published generated artifacts and SBOM data using automated CI/CD pipeline templates.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and signs SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.

       | Implemented: Gitlab Dependency Scanning natively generates a CycloneDX SBOM of all open source and third- party components, dependencies, and licenses. The dependency inventory is available in the Gitlab Dependency List at the project and group level. GitLab Runners and Gitlab CI pipeline automation capture vulnerability findings and metadata in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report. SBOM data is published to the Gitlab Package Registry. GitLab CI pipelines provide versioned, standardized automation templates from all hosted project from the GitLab pipeline component catalog.
   * - :ref:`E2.C-13.2 <scenario-c-13>`
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are not compromised

       | Resilience’s Valint tool is used to verify SBOM signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates

       | Implemented: Resilience Valint generates and verifies SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.C-13.3 <scenario-c-13>`
     - Outputs are logged by the CI/CD pipeline.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.C-14.1 <scenario-c-14>`
     - Issues in container image software and configurations are identified.
     - | Resilience Valint CLI provided evidence collection of automated scanning and testing actions.

       | Gitlab Platform CI and Runners executed Gitlab Container Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.

     - | Implemented: Resilience Valint collects results from automated scanning and testing components then logs compliance status.

       | Implemented: Gitlab Container Scanning identifies known vulnerabilities in the packages and dependencies in container images. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.C-14.2 <scenario-c-14>`
     - Source code and libraries are analyzed for defects, vulnerabilities, licensing issues, and code standard violations; outputs are logged.
     - | Resilience Valint CLI provided evidence collection of automated scanning and testing actions.

       | Gitlab Platform Pipelines and Runners executed Gitlab Advanced SAST and Gitlab Dependency Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard, Code Quality Report, and Vulnerability Report.

     - | Implemented: Resilience Valint collects results from automated scanning and testing components then logs compliance status. Note: Resilience Platform provides automated operation of security tools components. Resilience Platform was not implemented as part of this demonstration.

       | Implemented: Gitlab Advanced SAST and Dependency Scanning and native analyzers identify defects, vulnerabilities, and licensing issues in source code and libraries. GitLab Code Quality runs open-source analyzers to capture code quality and framework issues. GitLab Runners and Gitlab CI pipeline automation capture vulnerability with full scan output in CI job logs. These findings are also shown in the project’s Security tab, merge request widget, Gitlab Platform Security Dashboard, Code Quality Report, and Vulnerability Report.
   * - :ref:`E2.C-14.3 <scenario-c-14>`
     - Logs of container scanner results, including issues, are produced.
     - | Resilience Valint CLI provided evidence collection of automated scanning and testing actions.

       | Gitlab Platform Pipelines and Runners executed Gitlab Container Scanning. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard, Code Quality Report, and Vulnerability Report.

     - | Implemented: Resilience Valint collects results from automated scanning and testing components then logs compliance status. Note: Resilience Platform provides automated operation of security tools components. Resilience Platform was not implemented as part of this demonstration.

       | Implemented: Gitlab Container Scanning identifies known vulnerabilities in the packages and dependencies in container images. GitLab Runners and Gitlab CI pipeline automation capture vulnerability with full scan output in CI job logs. These findings are also shown in the project’s Security tab, merge request widget, and Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.C-15.1 <scenario-c-15>`
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code repositories based on user attributes and risk evaluation.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and access to branches were restricted to authorized users through the Gitlab Enforcer component.
   * - :ref:`E2.C-15.2 <scenario-c-15>`
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code repositories based on user attributes and classification level.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and authorization to approve merge requests and perform similar actions was restricted to authorized users through the Gitlab Enforcer component.
   * - :ref:`E2.C-15.3 <scenario-c-15>`
     - Infrastructure attributes (VMs, hosts, OS, etc.) meet the policy requirements and CI/CD pipelines are allowed to execute.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted pipeline execution to authorized CI/CD runners and build machines.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and the usage of pipeline runners was restricted to authorized runners and build machines through the Gitlab Enforcer component.
   * - :ref:`E2.C-15.4 <scenario-c-15>`
     - Secure communication is created between secrets/credential management tools and the build environment.
     - CyberArk Privilege Cloud, Secrets Manager, and Machine Identity Security securely share secrets with authorized entities during the Build Phase.
     - | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored and provided to authorized requestors.
   * - :ref:`E2.C-15.5 <scenario-c-15>`
     - | Users with the required clearance can make changes to classified branches while those with lower clearance are denied access. Push and pull requests are logged for audit purposes.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code branches based on user attributes and classification level.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Both access and changes to classified branches were restricted to authorized users through the Gitlab Enforcer component. The Gitlab Enforcer also logged all push and pull requests, along with the policy evaluation results.
   * - :ref:`E2.C-15.6 <scenario-c-15>`
     - Merge requests should only succeed when the classification level requirements are met. Merge requests are logged for audit purposes.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted merge request approval based on user attributes and branch classification level.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Merge requests were only allowed to proceed when approved by an authorized user.
       | The Gitlab Enforcer also logged all merge request attempts, along with the policy evaluation results.
   * - :ref:`E2.C-15.7 <scenario-c-15>`
     - System service accounts’ access to build systems and applications are allowed or denied based on ZT policies.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code repositories based on service account attributes and risk evaluation.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Access to code repositories was only allowed when the requesting service account passed the policy evaluation. The Gitlab Enforcer also logged all merge request attempts, along with the policy evaluation results.
   * - :ref:`E2.C-15.8 <scenario-c-15>`
     - Build processes should only succeed when the container images are pulled from approved image registries specified in the ZT policies.
     - | NextLabs’ CloudAz and NextLabs’ Gitlab Enforcer components restricted build processes to using specific authorized image registries based on project classification level.
     - | Implemented: ZT policy was written and defined within NextLabs CloudAz. The existing pipeline’s build job was hooked to poll the GitLab Enforcer with contents of Dockerfile. Build processes were blocked by the NextLabs Gitlab Enforcer if container images referenced did not conform to ZT policy requirements.
   * - :ref:`E2.C-15.9 <scenario-c-15>`
     - | Build artifacts are scanned for sensitive secrets before being allowed to leave the build process. Unapproved artifacts containing secrets not whitelisted by the ZT policies are prevented from leaving the build environment.
     - NextLabs’ CloudAz and Gitlab Enforcer components prevent build artifacts containing unapproved certificate or key files from promotion to the registry.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. A new pipeline job was created to inspect the contents of the built image and send it to the GitLab Enforcer. Build processes were blocked by the Gitlab Enforcer if unapproved artifacts were detected.
   * - :ref:`E2.C-15.10 <scenario-c-15>`
     - Trusted communication is enforced across build systems using certificate-based authentication.
     - NextLabs was supported by API-based authentication.
     - Partially Implemented: API-based authentication was implemented to support NextLabs’ CloudAZ and GitLab Enforcer. Trusted communication with certificate-based authentication will be included in a future Example Implementation.
   * - :ref:`E2.C-16.1 <scenario-c-16>`
     - Source code and configuration files are updated with generated changes and documented explanations.
     - | Gitlab Duo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

       | Sagittal Neo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

     - | Implemented: Gitlab Duo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.
   * - :ref:`E2.C-16.2 <scenario-c-16>`
     - Gaps and remediations for required standards are identified and provided as feedback.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.C-16.3 <scenario-c-16>`
     - Changes and explanations for external dependency risks are generated and documented.
     - | Gitlab Duo generated documentation and changes for container images and software packages based on security scanning and reports.

       | Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.

     - | Implemented: Gitlab Duo provides changes to source code and configuration while also generating documentation and explanations, which are based on
       | security scan output and generated security reports.

       | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output and generated security reports.
   * - :ref:`E2.C-16.4 <scenario-c-16>`
     - Exposed secrets are identified, and feedback is provided to remediate improper storage or disclosure.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.

.. _e2-test-results:

E2 Test Phase
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.D-1.1 <scenario-d-1>`
     - The test environment is provisioned, so that the updated software can be tested.
     - | CyberArk Machine Identity Security provisions TLS certificates from Zero-Touch PKI to secure communication within the test environment infrastructure.

       | Gitlab Platform CI provided CI/CD Pipelines for conducting automated testing activities

     - | Implemented: CyberArk Machine Identity Security provided TLS certificates used by runtime web services.

       | Implemented: Gitlab CI provides automation processes and tools for testing activities.
   * - :ref:`E2.D-1.2 <scenario-d-1>`
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - | Gitlab Platform Runners feature automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners feature automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings.
     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.D-1.3 <scenario-d-1>`
     - | Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the test process.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.D-1.4 <scenario-d-1>`
     - The resources used for the test environment have been freed up – no VMs, Containers, tools, or other environment components are still provisioned.
     - Gitlab Platform Environments provided separate configurations for maintaining isolated build environments.
     - Implemented: Gitlab Environments are defined for build environments to maintain isolation and parallel configurations.
   * - :ref:`E2.D-2 <scenario-d-2>`
     - Refer to results for E2.C3.
     - Refer to results for E2.C3.
     - Refer to results for E2.C3.
   * - :ref:`E2.D-3.1 <scenario-d-3>`
     - SCA identifies security vulnerabilities and compliance issues before third-party artifacts are used.
     - | Gitlab Platform Runners feature automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SCA findings.
     - | Implemented: Gitlab Runners provides SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.D-3.2 <scenario-d-3>`
     - SAST identifies security vulnerabilities and compliance issues before internal artifacts can be used.
     - Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings.
     - Implemented: Gitlab Runners provides Gitlab Advanced SAST scanning actions block downstream automation in the event that SAST scans are failing.
   * - :ref:`E2.D-3.3 <scenario-d-3>`
     - Issues are created in the ticketing system and logs of changes are maintained.
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings. Gitlab Platform Runners automated Gitlab Dependency Scan (SCA) actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured SAST and SCA findings. Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes
     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST and SCA dependency scanning actions of generated artifacts and captures detected vulnerabilities which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report. Gitlab Issues provides direct integration with Security Dashboard and Vulnerability Report to generate new issues from documented findings. Gitlab Issues to provides functionality to generate new issues from completed testing jobs.
   * - :ref:`E2.D-4.1 <scenario-d-4>`
     - Unit tests are pulled from SCM and ran successfully against known functional criteria.
     - Gitlab Platform Runners automated project unit testing actions and logged findings. Gitlab CI captured unit test findings in Unit Test Reports.
     - Implemented: Gitlab Runners provided automated project unit testing and captured findings which are recorded in Gitlab CI Unit Test Reports.
   * - :ref:`E2.D-4.2 <scenario-d-4>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results including issues (e.g., defects) in the ticketing system. Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output. Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     -
     - | Implemented: Gitlab CI captures output from automated test activities and provides integrations with Gitlab Issues to generate new issues from completed test jobs.
   * - :ref:`E2.D-5.1 <scenario-d-5>`
     - Regression test scripts are pulled from SCM and run successfully against known regression criteria.
     - Gitlab Platform Runners automated regression testing actions and logged findings.
     - Implemented: Gitlab Runners provides regression test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-5.2 <scenario-d-5>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - Implemented: Gitlab Runners provides regression test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-6.1 <scenario-d-6>`
     - Integration test scripts are pulled from SCM and run successfully against known integration criteria.
     - Gitlab Platform Runners automated integration testing actions and logged findings.
     - Implemented: Gitlab Runners provides integration test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-6.2 <scenario-d-6>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform provided Issues and Labels to capture defects for problems found.
     - Implemented: GitLab Issues and Labels help track issue statuses, organize work items, and categorize discovered defects.
   * - :ref:`E2.D-7.1 <scenario-d-7>`
     - Acceptance test scripts are pulled from SCM and run successfully against known acceptance criteria.
     - Gitlab Platform Runners automated acceptance testing actions and logged findings.
     - Implemented: Gitlab Runners provides acceptance test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-7.2 <scenario-d-7>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform provided Issues and Labels to capture defects for problems found.
     - Implemented: GitLab Issues and Labels help track issue statuses, organize work items, and categorize discovered defects.
   * - :ref:`E2.D-8.1 <scenario-d-8>`
     - Smoke test scripts are pulled from SCM and run successfully against known smoke test criteria.
     - Gitlab Platform Runners automated smoke testing actions and logged findings.
     - Implemented: Gitlab Runners provides smoke test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-8.2 <scenario-d-8>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform provided Issues and Labels to capture defects for problems found.
     - Implemented: GitLab Issues and Labels help track issue statuses, organize work items, and categorize discovered defects.
   * - :ref:`E2.D-9.1 <scenario-d-9>`
     - DAST tests are run successfully against security criteria.
     - Gitlab Platform Runners automated DAST actions and logged findings.
     - Implemented: Gitlab Runners provides DAST actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-9.2 <scenario-d-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.D-9.3 <scenario-d-9>`
     - Output of report is inspected for vulnerability severity (e.g., CVE/CVSS score).
     - | NextLabs’ CloudAz and Gitlab Enforcer components reviewed DAST scan findings and counted Medium, High, and Critical vulnerabilities before passing the counts to the NextLabs PDP.
     - | Implemented: ZT policy was written in NextLabs’ CloudAz to scan and review the output of DAST scans within each Gitlab pipeline. Information on detected vulnerabilities was passed on to the NextLabs’ PDP to inform the enforcement of ZT policy.
   * - :ref:`E2.D-10.1 <scenario-d-10>`
     - Acceptance or Integration test scripts are pulled from SCM and run successfully against known integration criteria.
     - Gitlab Platform Runners automated acceptance or integration testing actions and logged findings.
     - Implemented: Gitlab Runners provides acceptance or integration test actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-10.2 <scenario-d-10>`
     - IAST is run successfully against known security criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.D-10.3 <scenario-d-10>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.D-11.1 <scenario-d-11>`
     - Fuzz testing is run successfully.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.D-11.2 <scenario-d-11>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.D-12.1 <scenario-d-12>`
     - API testing is run successfully.
     - Gitlab Platform Runners automated DAST API actions and logged findings.
     - Implemented: Gitlab Runners provides DAST API actions of generated artifacts and captures detected findings.
   * - :ref:`E2.D-12.2 <scenario-d-12>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.D-13.1 <scenario-d-13>`
     - The pipeline stops when the code violates the policy.
     - Gitlab Pipeline Execution Policies provided pipeline enforcement to control pipeline execution context and configuration.
     - Implemented: Gitlab Pipeline Execution Policies provides execution configuration, required stages, and status monitoring.
   * - :ref:`E2.D-13.2 <scenario-d-13>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.D-14.1 <scenario-d-14>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.D-14.2 <scenario-d-14>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.D-15.1 <scenario-d-15>`
     - Software components are digitally signed, and secrets are stored and protected by HSM.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use by authorized code signing entities during the Test Phase.

       | Resilience’s Valint tool is used to sign software components. Resilience’s Attestation Store securely stores signatures and related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies signatures using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.D-15.2 <scenario-d-15>`
     - Signed software components are authentic and not tampered with.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use by authorized code signing entities during the Test Phase.

       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies signatures using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.D-15.3 <scenario-d-15>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.D-16.1 <scenario-d-16>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - | Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use by authorized code signing entities during the Test Phase.

       | Resilience’s Valint tool is used to generate SLSA artifacts. Resilience’s Attestation Store securely stores SLSA artifacts.

     - | Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SLSA artifacts using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.D-16.2 <scenario-d-16>`
     - Logs of results are available for tracking the integrity of the supply chain.
     - Gitlab CI provided CI/CD Pipelines to capture evidence and to associate evidence with Gitlab Release artifacts.
     - Implemented: Gitlab CI was leveraged to capture supply chain evidence and to attach evidence to artifacts hosted as Gitlab Releases.
   * - :ref:`E2.D-17.1 <scenario-d-17>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | CyberArk Machine Identity Security provided code signing certificates to support SBOM signing. Signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to generate and sign SBOMs related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.D-17.2 <scenario-d-17>`
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use by authorized code signing entities during the Test Phase.

       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.D-17.3 <scenario-d-17>`
     - Outputs are logged by the CI/CD pipeline.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all build phase actions for CI/CD Pipelines.
   * - :ref:`E2.D-18.1 <scenario-d-18>`
     - Users’ access to systems and applications are allowed or denied based on ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

       | NextLabs’ SkyDRM, CloudAz, and Gitlab Enforcer components limited development workstations and CI/CD runners usage to only authorized users.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and access to code repositories were restricted to authorized users through the SkyDRM, Windows Enforcer, and Gitlab Enforcer components.
   * - :ref:`E2.D-18.2 <scenario-d-18>`
     - A subset of users, with privileges to approve source codes and accept updates to artifact repositories are allowed access.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code repositories based on user attributes and classification level.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and merge requests to branches were restricted to authorized users through the Gitlab Enforcer component.
   * - :ref:`E2.D-18.3 <scenario-d-18>`
     - | Update ZT solutions to apply policies to the DevSecOps infrastructure (e.g., VMs, host, OS’s, etc.) so that the CI/CD pipelines will run only if infrastructure meets policy requirements.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted pipeline execution to authorized CI/CD runners and build machines.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and the usage of pipeline runners was restricted to authorized runners and build machines through the Gitlab Enforcer component.
   * - :ref:`E2.D-18.4 <scenario-d-18>`
     - Secure communication is created between secret/credential management tools and the test environment.
     - CyberArk Privilege Cloud, Secrets Manager, and Machine Identity Security securely share secrets with authorized entities during the Test Phase.
     - | Implemented: CyberArk Privilege Cloud and Secrets Hub securely store service account and API credentials. These credentials are provided to authorized requestors.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.
   * - :ref:`E2.D-18.5 <scenario-d-18>`
     - Failing mandatory tests specified in ZT policies are blocked from advancing.
     - NextLabs’ CloudAz and NextLabs’ Gitlab Enforcer components block pipeline progression if mandatory tests fail.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. A new pipeline job was created to poll the GitLab Enforcer with tests in the pipeline. Pipeline progression was blocked by the Gitlab Enforcer if tests defined in ZT policy were not found in the running pipeline.
   * - :ref:`E2.D-18.6 <scenario-d-18>`
     - | Test Phase communications are secured using certificate-based authentication. Token-based authentication usage is limited and adheres to best practices, including rotation and short expiration times.
     - NextLabs was sup-ported by API-based authentication.
     - Partially Implemented: API-based authen-tication was implemented to support NextLabs’ CloudAZ and GitLab Enforcer. Machine identity with certificate-based authentication and lifecycle management controls will be included in a future Exam-ple Implementation.
   * - :ref:`E2.D-18.7 <scenario-d-18>`
     - Job logs are monitored for specific keywords based on ZT policy
     - Nextlabs’ Gitlab Enforcer creates incident reports for specific keywords in job logs
     - | Implemented: ZT policy was written and defined within CloudAz. A GitLab job is hooked and polls the Gitlab Enforcer on success. The GitLab Enforcer then retrieves its job logs which are scanned for keywords defined in ZT policy. If these keywords are found, then an incident report is created.
   * - :ref:`E2.D-18.8 <scenario-d-18>`
     - | CI/CD pipeline progression is blocked or allowed based on GitLab DAST API severity findings. ZT policy defines thresholds for critical, high, and medium severity.
     - NextLabs' GitLab Enforcer counts severity findings in GitLab DAST API and allows or blocks pipelines based on ZT policy.
     - | Implemented: ZT policy was written and defined within CloudAz. A new pipeline job was created to poll the GitLab Enforcer on a successful security scan. NextLabs' GitLab Enforcer receives the GitLab DAST API report through successful GitLab job artifacts, counts findings by severity, and reports findings to the PDP. Depending on ZT policy, the NextLabs' GitLab Enforcer uses the PDP decision to allow or block the pipeline.
   * - :ref:`E2.D-18.9 <scenario-d-18>`
     - | CI/CD pipeline is blocked or allowed based on GitLab container scanning, dependency scanning, and SAST findings. ZT policy defines exemptions and thresholds for critical, high, and medium severity.
     - NextLabs' GitLab Enforcer blocks or allows CI/CD pipelines using severity counts and vulnerability identifiers based on ZT policy.
     - | Implemented: ZT policy was written and defined within CloudAz. A new pipeline job was created to poll the GitLab Enforcer on successful security scans.
       | NextLabs' GitLab Enforcer receives GitLab container scanning, dependency scanning, and SAST reports through GitLab job artifacts. NextLabs’ GitLab
       | Enforcer deduplicates CVE IDs across the three scanner reports, then passes severity counts and vulnerability ID lists to the NextLabs PDP for evaluation. Depending on ZT policy, the NextLabs' GitLab Enforcer uses the PDP decision to allow or block the pipeline.
   * - :ref:`E2.D-19.1 <scenario-d-19>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - | Gitlab Duo generated remediations from feedback provided by failed testing actions.

       | Sagittal Neo generated remediations from feedback provided by failed testing actions.

     - | Implemented: Gitlab Duo and Flow Security agent provides source code and configuration changes based detected failures captured by testing components during this phase.

       | Implemented: Sagittal Neo provides source code and configuration changes based detected failures captured by testing components during this phase.
   * - :ref:`E2.D-19.2 <scenario-d-19>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.D-19.3 <scenario-d-19>`
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - | Gitlab Duo generated documentation and changes for container images and software packages based on security scanning and reports.

       | Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.

     - | Implemented: Gitlab Duo provides changes to source code and configuration while also generating documentation and explanations, which are based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output and generated security reports.
   * - :ref:`E2.D-19.4 <scenario-d-19>`
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - | Gitlab Duo generated remediations from feedback provided by failed testing actions.

       | Sagittal Neo generated remediations from feedback provided by failed testing actions.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on detected test failures and generated reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on detected test failures and generated reports.
   * - :ref:`E2.D-19.5 <scenario-d-19>`
     - Performance bottlenecks are identified, and optimizations are provided.
     - Demonstrations of performance monitoring and assessment are out of scope of example implementations.
     - Demonstrations of performance monitoring and assessment are out of scope of example implementations.
   * - :ref:`E2.D-19.6 <scenario-d-19>`
     - Security findings are summarized with actionable mitigation steps.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.

.. _e2-release-results:

E2 Release Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 40 63

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.E-1.1 <scenario-e-1>`
     - The release environment is provisioned, so that the updated software can be released.
     - | Gitlab Platform CI provided CI/CD Pipelines for conducting automated release activities.

       | CyberArk Machine Identity Security provisions TLS certificates from Zero-Touch PKI to secure communication within the release environment infrastructure.

     - | Implemented: Gitlab CI provides automation processes and tools for release activities.

       | Implemented: CyberArk Machine Identity Security provided TLS certificates used by runtime web services.
   * - :ref:`E2.E-1.2 <scenario-e-1>`
     - CI/CD Pipelines run all test process components, and each component generates output for tracking status and logging detailed information.
     - Gitlab Platform Runners automated release actions and logged findings.
     - Implemented: Gitlab Runners provides release actions of generated artifacts and captures detected findings.
   * - :ref:`E2.E-1.3 <scenario-e-1>`
     - | Output that was logged by the CI/CD Pipelines is returned to Con-figuration Management Systems to track status and detailed information about the Release process.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines.
   * - :ref:`E2.E-2.1 <scenario-e-2>`
     - Artifacts created in this phase are securely stored in the Release phase artifact repository.
     - Gitlab Platform Container and Package Registry features provided storage for artifacts built by CI/CD Pipelines.
     - | Implemented: Gitlab Container and Package Registries provide release automation with a location to storage generated artifacts such as containers or software libraries.
   * - :ref:`E2.E-2.2 <scenario-e-2>`
     - Outputs are logged and artifacts can be released.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines.
   * - :ref:`E2.E-3.1 <scenario-e-3>`
     - Information (e.g., credentials and secrets) is maintained and secured by management systems.
     - | Microsoft Azure Entra ID provided storage and management functions for users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft AKV provided storage and management functions for certificates and secrets.

       | CyberArk Certificate Manager SaaS is leveraged for access and distribution of certificates

       | DigiCert Trust Lifecycle Manager is leveraged for access and distribution of certificates

     - | Implemented: Microsoft Azure Entra ID is leveraged to manage credentials. Microsoft AKV is leveraged to manage certificates and secrets.

       | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, manage, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided API keys and service connections to securely access stored certificates.
   * - :ref:`E2.E-3.2 <scenario-e-3>`
     - Logs and incidents are recorded.
     - Gitlab Platform Security Dashboard and Vulnerability Report displayed findings. Gitlab Platform CI provided CI/CD Pipelines to conduct automated actions.
     - | Implemented: Gitlab Security Dashboard and Vulnerability report logs and monitors status of identified risks and vulnerabilities. Gitlab CI provides job logs that capture output from automated actions.
   * - :ref:`E2.E-4.1 <scenario-e-4>`
     - Release packages are completed for distribution.
     - | Gitlab Platform Release provided collection and documentation mechanisms that include built software products, release evidence, and documentation for distribution.
     - Implemented: Gitlab Release provides distribution of built software packages, images, and binaries including collected evidence and documentation.
   * - :ref:`E2.E-4.2 <scenario-e-4>`
     - | Artifacts are organized, tracked, and secured. Software dependencies; Licensing analysis results; Bugs or defects; Security vulnerabilities

       | All software, including code, tools, and 3rd party libraries are running with the correct or expected versions.

     - | Gitlab Platform Release provided collection and documentation mechanisms that include built software products, release evidence, and documentation for distribution.
     - Implemented: Gitlab Release provides distribution of built software packages, images, and binaries including collected evidence and documentation.
   * - :ref:`E2.E-5.1 <scenario-e-5>`
     - Release information is collected and documented; Software dependencies, images, binaries, and software libraries are validated.
     - | Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output. Gitlab Platform Release provided collection and documentation mechanisms that include built software products, release evidence, and documentation for distribution. Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines. Gitlab Release provides distribution of built software packages, images, and binaries including collected evidence and documentation. Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.E-5.2 <scenario-e-5>`
     - Audit logs and compliance information are documented and provided to stakeholders.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines.
   * - :ref:`E2.E-6.1 <scenario-e-6>`
     - The results from the testing phase are gathered and put with the release.
     - | Gitlab Platform Job Artifacts provided storage of automated test results. Gitlab Platform Releases provided functionality to associate source code, binaries, release notes, and reports as a point-in-time release snapshot.
     - Implemented: Gitlab Release integrates with Job Artifact to associate testing results with release snapshots.
   * - :ref:`E2.E-7.1 <scenario-e-7>`
     - Smoke test scripts are pulled from SCM and run successfully against known smoke test criteria.
     - Gitlab Platform Runners automated smoke testing actions and logged findings.
     - Implemented: Gitlab Runners provides smoke testing actions of generated artifacts and captures detected findings.
   * - :ref:`E2.E-7.2 <scenario-e-7>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform provided Issues and Labels to capture defects for problems found.
     - Implemented: GitLab Issues and Labels help track issue statuses, organize work items, and categorize discovered defects.
   * - :ref:`E2.E-8.1 <scenario-e-8>`
     - Acceptance test scripts are pulled from SCM and run successfully against known acceptance criteria.
     - Gitlab Platform Runners automated acceptance testing actions and logged findings.
     - Implemented: Gitlab Runners provides acceptance testing actions of generated artifacts and captures detected findings.
   * - :ref:`E2.E-8.2 <scenario-e-8>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.E-9.1 <scenario-e-9>`
     - DAST tests are run successfully against security criteria.
     - | GitLab Platform CI and Runners executed GitLab DAST against the running applications. Findings are tracked in project’s Security tab, merge requests, and Gitlab Platform Security Dashboard and Vulnerability Report.
     - | Implemented: GitLab DAST scans capture runtime vulnerabilities for deployed applications. GitLab Runners and Gitlab CI pipeline automation capture vulnerability findings and metadata in the project’s Security tab, merge request widget, and dependency inventory in the Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.E-9.2 <scenario-e-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes.
     - | Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues or defects.
   * - :ref:`E2.E-9.3 <scenario-e-9>`
     - Acceptance test scripts are pulled from SCM and run successfully against known integration criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.E-9.4 <scenario-e-9>`
     - IAST is run successfully against known security criteria.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.E-9.5 <scenario-e-9>`
     - Output of reports is logged by the CI/CD Pipelines and returned to SCM providing results and issues (e.g., defects) are created for problems found.
     - This demonstration has been deferred to a future example implementation.
     - This demonstration has been deferred to a future example implementation.
   * - :ref:`E2.E-10.1 <scenario-e-10>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to imple-ment in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to imple-ment in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.E-10.2 <scenario-e-10>`
     - Logs of firmware updates or changes are captured
     - Components were not available to imple-ment in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to imple-ment in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.E-11.1 <scenario-e-11>`
     - | Software components and artifacts (e.g., commits, images, binaries, or libraries; Signature files) are digitally signed and secrets are stored and protected by HSM.
     - | Microsoft AKV provided storage and management functions for certificates.

       | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to sign and verify artifacts related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: Microsoft AKV is leveraged to manage certificates. Note: Microsoft AKV supports HSM-backed storage (Managed HSM) but was not implemented in Example Implementation 2.

       | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies signatures using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.E-11.2 <scenario-e-11>`
     - Results confirm that software components and artifacts are authentic and not tampered with.
     - CyberArk Certificate Manager SaaS provides monitoring and scanning to verify that certificates are not compromised.
     - Implemented: CyberArk Certificate Manager SaaS provided the Insight dashboard to monitor and identify at-risk certificates.
   * - :ref:`E2.E-11.3 <scenario-e-11>`
     - Detailed logging is captured and alerts sent to stakeholders.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines.
   * - :ref:`E2.E-12.1 <scenario-e-12>`
     - Issues in container image software and configurations are identified.
     - Resilience Valint CLI provided evidence collection of automated scanning and release actions.
     - Implemented: Resilience Valint collects results from automated scanning and release components then logs compliance status.
   * - :ref:`E2.E-12.2 <scenario-e-12>`
     - Source code and libraries are analyzed for defects, vulnerabilities, licensing issues, and code standard violations; outputs are logged.
     - Resilience Valint CLI provided evidence collection of automated scanning and release actions.
     - Implemented: Resilience Valint collects results from automated scanning and release components then logs compliance status.
   * - :ref:`E2.E-12.3 <scenario-e-12>`
     - Logs of container scanner results, including issues, are produced.
     - Resilience Valint CLI provided evidence collection of automated scanning and release actions.
     - Implemented: Resilience Valint collects results from automated scanning and release components then logs compliance status.
   * - :ref:`E2.E-12.4 <scenario-e-12>`
     - Images meeting security criteria are accepted.
     - Resilience Attestation Store provided documentation and identification of products and attestations that are out of compliance.
     - | Implemented: Resilience Attestation Store provided product integrations and search filters to help identify products and attestations that are failing policy requirements.
   * - :ref:`E2.E-13.1 <scenario-e-13>`
     - Supply-chain Levels for Software Artifacts (SLSA) Attestation successfully created.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to generate SLSA artifacts. Resilience’s Attestation Store securely stores SLSA artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SLSA artifacts using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.E-13.2 <scenario-e-13>`
     - Logs of results are available for tracking the integrity of the supply chain.
     - Gitlab CI provided CI/CD Pipelines to capture evidence and to associate evidence with Gitlab Release artifacts.
     - Implemented: Gitlab CI was leveraged to capture supply chain evidence and to attach evidence to artifacts hosted as Gitlab Releases.
   * - :ref:`E2.E-13.3 <scenario-e-13>`
     - SBOM contains all open-source and third-party components, dependencies, and licenses.
     - | CyberArk Machine Identity Security provided code signing certificates to support SBOM signing. Signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to generate and sign SBOMs related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.E-13.4 <scenario-e-13>`
     - Confirm SBOM signatures to verify authenticity and integrity of all software artifacts.
     - | CyberArk Machine Identity Security provided code signing certificates to support artifact signing. Code signing materials are stored in an HSM until requested for use.

       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.

     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.

       | Implemented: Resilience Valint generates and verifies SBOMs using signing material provided by CyberArk Machine Identity Security. These artifacts are securely stored in the Resilience Attestation Store.
   * - :ref:`E2.E-13.5 <scenario-e-13>`
     - Outputs are logged by the CI/CD pipeline.
     - Gitlab Platform CI feature provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all release phase actions for CI/CD Pipelines.
   * - :ref:`E2.E-14.1 <scenario-e-14>`
     - IaC Scanner identifies security vulnerabilities and compliance issues before IaC is executed.
     - | Gitlab Platform Runners automated IaC scanning actions and logged findings. Gitlab Platform Security Dashboard and Vulnerability Report captured IaC findings.
     - | Implemented: Gitlab Runners provides IaC scanning actions that generate vulnerability logs which are recorded in Gitlab Platform Security Dashboard and Vulnerability Report.
   * - :ref:`E2.E-14.2 <scenario-e-14>`
     - Issues are created and resolved, and logs of changes are maintained.
     - Gitlab Platform provided Issues and Tasks to track remediation work and document changes, organized with Labels, Boards, and Milestones.
     - Implemented: GitLab Issues and Tasks organize items with Labels, Boards and Milestones while capturing full change histories of each work item.
   * - :ref:`E2.E-14.3 <scenario-e-14>`
     - Release environment is provisioned and managed based on scanned IaC artifacts to ensure consistency.
     - Gitlab Platform CI provided linked CI/CD Pipelines that can automatically deploy environment updates.
     - Implemented: Gitlab CI provides automated deployment of default branches or specific environments based on approved and merged IaC changes.
   * - :ref:`E2.E-15.1 <scenario-e-15>`
     - Users’ access to release systems and applications are allowed or denied based on ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | CyberArk Secure Infrastructure Access controls access to release servers with zero-trust policies.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.

       | Implemented: CyberArk Secure Infrastructure Access managed access to release servers based on identities provided by Entra ID.
   * - :ref:`E2.E-15.2 <scenario-e-15>`
     - Infrastructure meets the policy requirements and tools are allowed to execute.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted pipeline execution to authorized CI/CD runners and release servers.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz, and the usage of pipeline runners was restricted to authorized runners and build machines through the Gitlab Enforcer component.
   * - :ref:`E2.E-15.3 <scenario-e-15>`
     - | Secrets, credentials, and variables stored on the file system are protected and shared securely. Communications between systems are secured by ZT policies.
     - | CyberArk Certificate Manager SaaS is leveraged for access and distribution of certificates.

       | DigiCert Trust Lifecycle Manager is leveraged for access and distribution of certificates.

     - | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, managed, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided certificates, service accounts, and applications to securely access, managed, and store certificates.
   * - :ref:`E2.E-15.4 <scenario-e-15>`
     - Only software proven to originate from the approved build and test phase processes in compliance with ZT policies are staged for release.
     - | NextLabs’ CloudAz and Gitlab Enforcer components ensure that all required evidence jobs have been completed successfully before the software is published. NextLabs’ Gitlab Enforcer receives dependency SBOM from the Gitlab dependency scanning job and checks for packages with invalid purl or version. NextLabs’ Gitlab Enforcer also reviews DAST scan results and blocks pipe-line progression when results fail to meet ZT policy criteria.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Release phase progression was blocked by the Gitlab Enforcer if required evidence tests failed. A new pipeline job was created to depend on the GitLab dependency scanning job and poll the GitLab Enforcer with the report on successful run. Gitlab Enforcer receives dependency SBOM and checks for packages with invalid purl or version. If non-whitelisted invalid packages are found, release is blocked. NextLabs’ Gitlab Enforcer counts Medi-um, High, and Critical vulnerabilities be-fore passing the counts to the NextLabs PDP. Any such finding blocks progression, preventing release of applications with known exploitable vulnerabilities.
   * - :ref:`E2.E-16.1 <scenario-e-16>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.E-16.2 <scenario-e-16>`
     - Test failures are reported with diagnostic feedback and remediation suggestions.
     - | Gitlab Duo generated remediations from feedback provided by failed testing actions.

       | Sagittal Neo generated remediations from feedback provided by failed testing actions.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on detected test failures and generated reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on detected test failures and generated reports.
   * - :ref:`E2.E-16.3 <scenario-e-16>`
     - Change recommendations, explanations, and suggestions are produced for software libraries and external dependencies.
     - | Gitlab Duo generated documentation and changes for container images and software packages based on security scanning and reports.

       | Sagittal Neo generated documentation and changes for container images and software packages based on security scanning and reports.

     - | Implemented: Gitlab Duo provides changes to source code and configuration while also generating documentation and explanations, which are based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides changes to source code (e.g., commits, branches, and pull/merge requests) and configuration while also generating documentation and explanations, which are based on security scan output and generated security reports.
   * - :ref:`E2.E-16.4 <scenario-e-16>`
     - | Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure of sensitive certificates, secrets, or credentials.
     - | Gitlab Duo generated code and configuration changes based on security and other compliance requirements.

       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.

     - | Implemented: Gitlab Duo provides code and configuration changes based on detected security findings that require remediation.

       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings that require remediation.
   * - :ref:`E2.E-16.5 <scenario-e-16>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.E-16.6 <scenario-e-16>`
     - Plans are generated and provide methods to mitigate or remediate vulnerabilities found in artifacts.
     - | Gitlab Duo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

       | Sagittal Neo generated source code, configuration, and documentation changes for Gitlab-hosted projects.

     - | Implemented: Gitlab Duo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.
       | Implemented: Sagittal Neo provides generated content based on existing source code, configuration files, and project documentation associated with Gitlab source code repositories.

.. _e2-deploy-results:

E2 Deploy Phase
^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.F-1.1 <scenario-f-1>`
     - The deployment environment is provisioned, so that the updated software can be deployed.
     - | Gitlab Platform CI provided CI/CD Pipelines for conducting automated deploy activities.
       | CyberArk Machine Identity Security provisions TLS certificates from Zero-Touch PKI to secure communication within the deploy environment infrastructure.
     - | Implemented: Gitlab CI provides automation processes and tools for deploy phase activities.
       | Implemented: CyberArk Machine Identity Security provided TLS certificates used by runtime web services.
   * - :ref:`E2.F-1.2 <scenario-f-1>`
     - CI/CD Pipelines run all deployment process components, and each component generates output for tracking status and logging detailed information.
     - Gitlab Platform Runners automated release actions and logged findings.
     - Implemented: Gitlab Runners provides deploy actions of generated artifacts and captures detected findings.
   * - :ref:`E2.F-1.3 <scenario-f-1>`
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track configuration status and detailed information about the Release process.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all deploy phase actions for CI/CD Pipelines.
   * - :ref:`E2.F-2 <scenario-f-2>`
     - Refer to results of E2.E-2.
     - Refer to results of E2.E-2.
     - Refer to results of E2.E-2.
   * - :ref:`E2.F-3 <scenario-f-3>`
     - Refer to results of E2.E-3.
     - Refer to results of E2.E-3.
     - Refer to results of E2.E-3.
   * - :ref:`E2.F-4 <scenario-f-4>`
     - Refer to results of E2.E-5.
     - Refer to results of E2.E-5.
     - Refer to results of E2.E-5.
   * - :ref:`E2.F-5 <scenario-f-5>`
     - Refer to results of E2.E-14.
     - Refer to results of E2.E-14.
     - Refer to results of E2.E-14.
   * - :ref:`E2.F-6.1 <scenario-f-6>`
     - SBOM and other provenance data are verified before deployment.
     - | Gitlab Platform CI provided CI/CD Pipelines for conducting automated deploy activities.
       | Resilience Valint CLI verifies signed SBOMs that contain a list of dependencies and artifact metadata.
     - | Implemented: Gitlab CI provides automation processes and tools for deploy phase activities.
       | Implemented: Resilience Valint verifies the data contained in SBOM artifacts and artifact metadata and verifies associated signatures in accordance with required policies.
   * - :ref:`E2.F-6.2 <scenario-f-6>`
     - Output that was logged by the CI/CD Pipelines is returned to Configuration Management Systems to track status and detailed information about the SBOM process.
     - Gitlab Platform CI provided CI/CD Pipelines to capture automated actions and save pipeline output.
     - Implemented: Gitlab CI was leveraged to capture and log output from all deploy phase actions for CI/CD Pipelines.
   * - :ref:`E2.F-7.1 <scenario-f-7>`
     - Results confirm that firmware components and artifacts are authentic and not tampered with.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.F-7.2 <scenario-f-7>`
     - Software components and artifacts that are verified are accepted.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.F-7.3 <scenario-f-7>`
     - Firmware is up to date on all hardware components.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.F-8.1 <scenario-f-8>`
     - Users’ access to the deploy phase environment are allowed or denied based on ZT policies.
     - Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.
     - Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.
   * - :ref:`E2.F-8.2 <scenario-f-8>`
     - System-to-system communications are restricted based on functionality and ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.
       |
       | NextLabs’ SkyDRM, CloudAz, and Gitlab Enforcer components limited development workstations and CI/CD runners’ usage to only authorized users.
     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and policies alongside network and resource access controls to restrict system and resource communications within an environment.
       |
       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz and access to code repositories were restricted to authorized users through the SkyDRM, Windows Enforcer, and Gitlab Enforcer components.
   * - :ref:`E2.F-8.3 <scenario-f-8>`
     - Only signed and validated software can be deployed based on ZT policies.
     - | CyberArk Machine Identity Security provided code signing certificates to support validation of signed software. Code signing materials are stored in an HSM until requested for use.
       |
       | NextLabs’ CloudAz and Gitlab Enforcer components require that software successfully completes signature validation checks before deployment.
       |
       | Resilience’s Valint tool is used to verify signatures related to software components. Resilience’s Attestation Store securely stores related artifacts.
     - | Implemented: CyberArk Code Sign Manager generates code signing material using a CyberArk Zero Touch PKI Certificate Authority. This code signing material is securely stored within an HSM and provided to authorized requestors.
       |
       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Deployment processes were blocked by the Gitlab Enforcer if signature validation tests resulted in failure.
       |
       | Implemented: Resilience’s Valint tool was used to validate container signatures, SBOM signatures, and SLSA compliance signatures. These were retrieved from secure storage in the Resilience Attestation Store.
   * - :ref:`E2.F-8.4 <scenario-f-8>`
     - Deployment is controlled for projects with data residency requirements based on ZT policy
     - NextLabs’ Gitlab Enforcer receives information from Gitlab pipeline deployment jobs to enforce data residency requirements
     - Implemented: ZT policy was written and defined within CloudAz. The existing pipeline deployment job was hooked to poll the GitLab Enforcer with Kubernetes deployment information. Gitlab Enforcer receives this information and blocks deployments for projects with non-whitelisted regions based on ZT policy.
   * - :ref:`E2.F-9.1 <scenario-f-9>`
     - Suggestions and remediation guidance are provided and documented for the identified deployment issues.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.
       |
       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.
       |
       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.F-9.2 <scenario-f-9>`
     - Mitigations for risks, threats, and vulnerabilities are documented in risk management system or threat modeling tools.
     - | Gitlab Duo provided analysis of risks and vulnerabilities provided as context from Gitlab Security Dashboard and Vulnerability Report.
       |
       | Sagittal Neo provided analysis of risks and vulnerabilities provided as context from Gitlab Security Dashboard and Vulnerability Report.
     - | Implemented: Gitlab Duo provides generated content based on associated security requirements included Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.
       |
       | Implemented: Sagittal Neo provides generated content based on associated security requirements included Work Items and Issues created by the Gitlab Security Dashboard and Vulnerability Report.
   * - :ref:`E2.F-9.3 <scenario-f-9>`
     - Exposed secrets are identified, and steps are provided to help remediate improper storage and potential disclosure.
     - | Gitlab Duo generated code and configuration changes based on security and other compliance requirements.
       |
       | Sagittal Neo generated code and configuration changes based on security and other compliance requirements.
     - | Implemented: Gitlab Duo provides code and configuration changes based on detected security findings that require remediation.
       |
       | Implemented: Sagittal Neo provides code and configuration changes based on detected security findings that require remediation.
   * - :ref:`E2.F-9.4 <scenario-f-9>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.
       |
       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.
     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.
       |
       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.F-9.5 <scenario-f-9>`
     - Configuration changes are generated in configuration management system.
     - Components were not available to implement in this demonstration. Configuration Management System will be included in future example implementation.
     - Components were not available to implement in this demonstration. Configuration Management System will be included in future example implementation.
   * - :ref:`E2.F-9.6 <scenario-f-9>`
     - Deployment status and scope notifications are generated and documented in project or deployment management systems.
     - Components were not available to implement in this demonstration. Configuration Management System will be included in future example implementation.
     - Components were not available to implement in this demonstration. Configuration Management System will be included in future example implementation.

.. _e2-operate-results:

E2 Operate Phase
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 37 66

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.G-1 <scenario-g-1>`
     - Refer to results for E2.F-1.
     - Refer to results for E2.F-1.
     - Refer to results for E2.F-1.
   * - :ref:`E2.G-2 <scenario-g-2>`
     - Refer to results for E2.F-7.
     - Refer to results for E2.F-7.
     - Refer to results for E2.F-7.
   * - :ref:`E2.G-3 <scenario-g-3>`
     - Refer to results for E2.E-13.
     - Refer to results for E2.E-13.
     - Refer to results for E2.E-13.
   * - :ref:`E2.G-4.1 <scenario-g-4>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.G-4.2 <scenario-g-4>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.G-4.3 <scenario-g-4>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.G-5.1 <scenario-g-5>`
     - Users’ access to the operate phase environment are allowed or denied based on ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.
   * - :ref:`E2.G-5.2 <scenario-g-5>`
     - System-to-system communications are restricted based on functionality and ZT policies.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized systems, users, and service accounts.

       | Microsoft Azure Network Security Groups were implemented to restrict network communication within the operate phase environment.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and policies alongside network and resource access controls to restrict system and resource communications within an environment.
   * - :ref:`E2.G-5.3 <scenario-g-5>`
     - Unauthorized changes and vulnerabilities are detected and reported based on the ZT policies.
     - | NextLabs’ CloudAz and Drift Response components monitor the application’s configuration and SBOM packages for changes and vulnerabilities, initiating a response if unauthorized modifications or vulnerabilities are detected.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. NextLabs Drift Response monitors both application configuration and reviews the SBOM for vulnerabilities in package versions by hooking the existing deployment jobs in the pipeline. If application configuration differs from known-good baseline an alert is generated. If SBOM vulnerabilities are detected, an alert is generated.
   * - :ref:`E2.G-6.1 <scenario-g-6>`
     - Suggestions and remediation guidance are provided and documented for the identified source code and configuration issues.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.
   * - :ref:`E2.G-6.2 <scenario-g-6>`
     - Gaps are reported with remediation guidance to achieve compliance with required baselines, standards, or frameworks.
     - | Gitlab Duo generated remediations from feedback provided by security scanning and reports.

       | Sagittal Neo generated remediations from feedback provided by security scanning and reports.

     - | Implemented: Gitlab Duo provides source code and configuration changes based on security scan output and generated security reports.

       | Implemented: Sagittal Neo provides source code and configuration changes based on security scan output and generated security reports.

.. _e2-continuous-improvements-results:

E2 Continuous Improvements, Security and Monitoring Phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 17 40 40 63

   * - Demo ID
     - Expected Outcome
     - Observed Outcome
     - Comments
   * - :ref:`E2.H-1 <scenario-h-1>`
     - Refer to results for E2.A-5-7, E2.A-6, E2.A-7, E2.F-1, and E2.F-3.
     - Refer to results for E2.A-5-7, E2.A-6, E2.A-7, E2.F-1, and E2.F-3.
     - Refer to results for E2.A-5-7, E2.A-6, E2.A-7, E2.F-1, and E2.F-3.
   * - :ref:`E2.H-2 <scenario-h-2>`
     - Refer to results for E2.A-1.
     - Refer to results for E2.A-1.
     - Refer to results for E2.A-1.
   * - :ref:`E2.H-3.1 <scenario-h-3>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Implemented: Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes. Gitlab Platform Security Dashboard and Vulnerability Report displayed findings.

       | TLS Certificate lifecycle is monitored and managed via CyberArk Machine Identity Security. 
     - | Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues, defects, and findings provided by Gitlab Security Dashboard and Vulnerability Report.

       | Implemented: CyberArk Machine Identity Security monitors lifecycle managed certificates used hosts and services.
   * - :ref:`E2.H-3.2 <scenario-h-3>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Implemented: Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes. Gitlab Platform Security Dashboard and Vulnerability Report displayed findings.
 
       | TLS Certificate lifecycle is monitored and managed via CyberArk Machine Identity Security. 
     - | Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues, defects, and findings provided by Gitlab Security Dashboard and Vulnerability Report.

       | Implemented: CyberArk Machine Identity Security monitors lifecycle managed certificates used hosts and services.
   * - :ref:`E2.H-4.1 <scenario-h-4>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - | Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes. Gitlab Platform Security Dashboard and Vulnerability Report displayed findings.
     - Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues, defects, and findings provided by Gitlab Security Dashboard and Vulnerability Report.
   * - :ref:`E2.H-4.2 <scenario-h-4>`
     - The monitoring system generates output for tracking status and logging detailed information. If an issue arises a ticket is created.
     - Gitlab Platform Issues provided Work Items, Issues, and Milestones to track issues and document changes. Gitlab Platform Security Dashboard and Vulnerability Report displayed findings.
     - Implemented: Gitlab Issues provides issue tracking via Work Items (boards), issues (lists), or Milestones (epics) to help document changes to project and to help track status of issues, defects, and findings provided by Gitlab Security Dashboard and Vulnerability Report.
   * - :ref:`E2.H-4.3 <scenario-h-4>`
     - The responsible disclosure of new vulnerabilities discovered by external sources.
     - Demonstration of process for disclosure of undiscovered vulnerabilities is out of scope of example implementations.
     - Demonstration of process for disclosure of undiscovered vulnerabilities is out of scope of example implementations.
   * - :ref:`E2.H-5.1 <scenario-h-5>`
     - Firmware is developed and managed.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.H-5.2 <scenario-h-5>`
     - Signed firmware artifacts are verified and authentic.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.H-5.3 <scenario-h-5>`
     - Logs of firmware updates or changes are captured.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
     - Components were not available to implement in this demonstration. Firmware Services will be included in future example implementation.
   * - :ref:`E2.H-6.1 <scenario-h-6>`
     - Update policies in ZT solution tools to provide access to users to release management systems and applications based on user needs.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments. Microsoft Entra Conditional Access policies were implemented to restrict access to authorized users.
     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and user policies alongside network and resource access controls to restrict access to systems and resources.
   * - :ref:`E2.H-6.2 <scenario-h-6>`
     - Update monitoring systems and automated tools with ZT policies to ensure systems communicate to other systems on a needed basis only.
     - | Microsoft Azure Entra ID provided policy management of users, groups, service accounts, and other service principals as well as roles and role assignments.

       | Microsoft Entra Conditional Access policies were implemented to restrict access to authorized systems, users, and service accounts.

       | Microsoft Azure Network Security Groups were implemented to restrict network communication within the operate phase environment.

     - | Implemented: Microsoft Azure Entra ID and Conditional Access policies provides role-based access control and policies alongside network and resource access controls to restrict system and resource communications within an environment.
   * - :ref:`E2.H-6.3 <scenario-h-6>`
     - Update ZT policies to restrict modifications to restricted branches to only the users that have the authorization to access them.
     - NextLabs’ CloudAz and Gitlab Enforcer components restricted access to code branches based on user attributes and classification level.
     - | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Both access and changes to classified branches were restricted to authorized users through the Gitlab Enforcer component. The Gitlab Enforcer also logged all push and pull requests, along with the policy evaluation results.
   * - :ref:`E2.H-6.4 <scenario-h-6>`
     - Update ZT solutions to integrate with software security tools (e.g., SAST, SCA, Lint tools).
     - | Gitlab Platform Runners automated Gitlab Advanced SAST scanning actions and logged findings.

       | NextLabs’ CloudAz and Gitlab Enforcer components block pipeline progression if mandatory tests (SAST, DAST, SCA, etc.) fail.

     - | Implemented: Gitlab Runners provides Gitlab Advanced SAST scanning actions block downstream automation in the event that SAST scans are failing.

       | Implemented: ZT policy was written and defined within NextLabs’ CloudAz. Pipeline progression was blocked by the Gitlab Enforcer if SAST, DAST, or other mandatory tests failed.
   * - :ref:`E2.H-6.5 <scenario-h-6>`
     - | Certificates, credentials, and secrets stored on the file system are protected and shared securely. Communications between systems are secured by ZT policies.
     - | CyberArk Certificate Manager SaaS is leveraged for access and distribution of certificates.

       | DigiCert Trust Lifecycle Manager is leveraged for access and distribution of certificates.

     - | Implemented: CyberArk Certificate Manager SaaS provided certificates, service accounts, and applications to securely access, managed, and store certificates.

       | Implemented: DigiCert Trust Lifecycle Manager provided certificates, service accounts, and applications to securely access, manage, and store certificates.
   * - :ref:`E2.H-6.6 <scenario-h-6>`
     - Unauthorized changes are detected and reported.
     - Refer to results for E2.G-5.3.
     - Refer to results for E2.G-5.3.
   * - :ref:`E2.H-7.1 <scenario-h-7>`
     - Risk reports are generated, and mitigation actions are triggered in risk management or ticketing systems.
     - | Gitlab Duo provided analysis of standards and frameworks provided as context.

       | Sagittal Neo provided analysis of standards and frameworks provided as context.

     - | Implemented: Gitlab Duo and Flow Security agent provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.

       | Implemented: Sagittal Neo provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.
   * - :ref:`E2.H-7.2 <scenario-h-7>`
     - Security alerts are correlated with logs, and corresponding remediation tickets are automatically generated.
     - | Gitlab Duo provided analysis of standards and frameworks provided as context.

       | Sagittal Neo provided analysis of standards and frameworks provided as context.

     - | Implemented: Gitlab Duo provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.

       | Implemented: Sagittal Neo provides generated content based on associated security compliance requirements included in assigned Work Items and Issues.
