<main>

  <div class="lang-switch">
    Langue / Language :
    <a href="#fr-changelog">FR</a> ·
    <a href="#en-changelog">EN</a>
  </div>

  <!-- ========================================================= -->
  <!-- ======================== FR ============================= -->
  <!-- ========================================================= -->

  <section id="fr-changelog">
    <h2>Changelog – Global HashCost Index (GHI)</h2>

    <p>
      Cette page résume les principales évolutions du standard GHI, de l’API publique
      et du moteur sandbox. Elle est destinée aux équipes techniques, aux intégrateurs
      et aux partenaires institutionnels.
    </p>

    <!-- v0.4.2-sandbox / API v1.1 -->
    <div class="card">
      <h3>2025-12-09 – Sandbox Engine v0.4.2 & API v1.1</h3>
      <p>
        Cette version marque la stabilisation du couple <strong>API publique v1.1</strong>
        + <strong>Sandbox Engine v0.4.2</strong>.
      </p>
      <ul>
        <li><strong>API publique v1.1</strong> déclarée comme version active et stable.</li>
        <li><strong>Sandbox Engine v0.4.2-sandbox</strong> :
          <ul>
            <li>un seul router v1.1 pour l’ensemble des endpoints <code>/v1/ghi/*</code> ;</li>
            <li>données synthétiques mises à jour pour <code>/snapshot</code> et <code>/history</code> ;</li>
            <li>métadonnées unifiées : <code>version</code>, <code>timestamp_utc</code>, <code>engine_sandbox_version</code> ;</li>
            <li>support complet des endpoints v1.1 : snapshot, history, regions, metadata, network, forecast.</li>
          </ul>
        </li>
        <li><strong>Documentation publique</strong> :
          <ul>
            <li>nouvelle page <strong>API v1.1</strong> : <code>api/api-v1.1.html</code> ;</li>
            <li>mise à jour de la page <strong>Moteur</strong> pour Sandbox v0.4.2 ;</li>
            <li>note technique publique : <code>ENGINE_DESIGN_CHANGES_v0.4.2.md</code>.</li>
          </ul>
        </li>
        <li><strong>Compatibilité</strong> :
          <ul>
            <li>aucun breaking change pour les intégrations v1.1 existantes ;</li>
            <li>API v1.0 maintenue en mode “legacy” (documentation disponible, mais non recommandée pour de nouveaux projets).</li>
          </ul>
        </li>
      </ul>
    </div>

    <!-- v0.4.0-sandbox / API v1.0 -->
    <div class="card">
      <h3>2025-01-XX – Sandbox Engine v0.4.0 & API v1.0 (baseline publique)</h3>
      <p>
        Première mise à disposition publique du standard GHI avec :
      </p>
      <ul>
        <li><strong>Standard GHI v1.0</strong> (modèle de données, méthodologie, transparence).</li>
        <li><strong>Sandbox Engine v0.4.0-sandbox</strong> :
          <ul>
            <li>premier moteur de démonstration avec régions synthétiques ;</li>
            <li>exposition des endpoints <code>/v1/ghi/snapshot</code>, <code>/v1/ghi/history</code> ;</li>
            <li>métadonnées de base.</li>
          </ul>
        </li>
        <li><strong>API publique v1.0</strong> :
          <ul>
            <li>structure initiale des réponses ;</li>
            <li>premier jeu de tests automatisés.</li>
          </ul>
        </li>
        <li><strong>Site GHI-public</strong> :
          <ul>
            <li>publication des pages standards : Accueil, Dashboard, Méthodologie, Transparence, Institutions, etc.</li>
          </ul>
        </li>
      </ul>
      <p>
        Cette version sert de baseline historique pour les évolutions ultérieures du standard.
      </p>
    </div>

    <div class="card">
      <h3>Politique de versionning</h3>
      <ul>
        <li>Les versions d’API suivent le schéma <code>MAJEUR.MINOR</code> (ex. v1.1).</li>
        <li>Le moteur sandbox suit sa propre numérotation <code>v0.x.y-sandbox</code>.</li>
        <li>Les changements majeurs sont documentés publiquement (site + GitHub).</li>
      </ul>
    </div>

  </section>

  <!-- ========================================================= -->
  <!-- ======================== EN ============================= -->
  <!-- ========================================================= -->

  <section id="en-changelog">
    <h2>Changelog – Global HashCost Index (GHI)</h2>

    <p>
      This page summarizes the main changes to the GHI standard, public API
      and sandbox engine. It targets technical teams, integrators and institutional partners.
    </p>

    <!-- v0.4.2-sandbox / API v1.1 -->
    <div class="card">
      <h3>2025-12-09 – Sandbox Engine v0.4.2 & API v1.1</h3>
      <p>
        This release stabilizes the combination of <strong>Public API v1.1</strong>
        and <strong>Sandbox Engine v0.4.2</strong>.
      </p>
      <ul>
        <li><strong>Public API v1.1</strong> declared as active and stable version.</li>
        <li><strong>Sandbox Engine v0.4.2-sandbox</strong>:
          <ul>
            <li>single v1.1 router for all <code>/v1/ghi/*</code> endpoints;</li>
            <li>refreshed synthetic data for <code>/snapshot</code> and <code>/history</code>;</li>
            <li>unified metadata: <code>version</code>, <code>timestamp_utc</code>, <code>engine_sandbox_version</code>;</li>
            <li>full support of v1.1 endpoints: snapshot, history, regions, metadata, network, forecast.</li>
          </ul>
        </li>
        <li><strong>Public documentation</strong>:
          <ul>
            <li>new <strong>API v1.1</strong> page: <code>api/api-v1.1.html</code>;</li>
            <li>updated <strong>Engine</strong> page for Sandbox v0.4.2;</li>
            <li>public technical note: <code>ENGINE_DESIGN_CHANGES_v0.4.2.md</code>.</li>
          </ul>
        </li>
        <li><strong>Compatibility</strong>:
          <ul>
            <li>no breaking changes for existing v1.1 integrations;</li>
            <li>API v1.0 kept as “legacy” (documented, but not recommended for new projects).</li>
          </ul>
        </li>
      </ul>
    </div>

    <!-- v0.4.0-sandbox / API v1.0 -->
    <div class="card">
      <h3>2025-01-XX – Sandbox Engine v0.4.0 & API v1.0 (public baseline)</h3>
      <p>
        First public availability of the GHI standard, including:
      </p>
      <ul>
        <li><strong>GHI Standard v1.0</strong> (data model, methodology, transparency).</li>
        <li><strong>Sandbox Engine v0.4.0-sandbox</strong>:
          <ul>
            <li>initial demo engine with synthetic regions;</li>
            <li>exposed <code>/v1/ghi/snapshot</code> and <code>/v1/ghi/history</code> endpoints;</li>
            <li>basic metadata.</li>
          </ul>
        </li>
        <li><strong>Public API v1.0</strong>:
          <ul>
            <li>initial response structure;</li>
            <li>first automated test suite.</li>
          </ul>
        </li>
        <li><strong>GHI-public website</strong>:
          <ul>
            <li>initial publication of core pages: Home, Dashboard, Methodology, Transparency, Institutions, etc.</li>
          </ul>
        </li>
      </ul>
      <p>
        This version acts as the historical baseline for future standard releases.
      </p>
    </div>

    <div class="card">
      <h3>Versioning policy</h3>
      <ul>
        <li>API versions follow <code>MAJOR.MINOR</code> (e.g. v1.1).</li>
        <li>The sandbox engine uses its own <code>v0.x.y-sandbox</code> numbering.</li>
        <li>Major changes are documented publicly (website + GitHub).</li>
      </ul>
    </div>

  </section>

</main>