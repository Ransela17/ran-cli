import click, json
from ran_cli.cli import Api


# --- Repositories Group command called repo  --- #
@click.group()
def cli():
    """Several commands to make operations on Jfrog Artifacts repositories"""
    pass

# --- Get Repositories command --- #
@cli.command()
@click.option('-t', '--type', type=click.Choice(["local", "remote", "virtual", "distribution"]), required=True, help="Most Provide the Type from the list: local|remote|virtual|distribution")
@click.option('-pt', '--packageType', type=click.Choice( ["maven","gradle","ivy","sbt","helm","cocoapods",
            "opkg","rpm", "nuget","cran","gems","npm","bower","debian","composer","pypi",
            "docker","vagrant","gitlfs","go","yum","conan","chef","puppet","generic",""]), default='', 
            help='Choose one of the following: maven|gradle|ivy|sbt|helm|cocoapods|opkg|rpm|nuget|cran|gems|npm|bower|debian|composer|pypi|docker|vagrant|gitlfs|go|yum|conan|chef|puppet|generic')
def list(type,packagetype):
    """ Returns a list of minimal repository details for all repositories of the specified type"""
    endpoint='/repositories/?type='+type+'&packageType='+packagetype
    response = Api.get_call(endpoint).json()
    click.echo(json.dumps(response, indent=4, sort_keys=True)) # Print the pretty response 

# --- Create Repository command --- #
@cli.command()
@click.option('-k', '--key', type=str, required=True)
@click.option('-p', '--packageType', type=click.Choice( ["maven","gradle","ivy","sbt","helm","cocoapods",
            "opkg","rpm", "nuget","cran","gems","npm","bower","debian","composer","pypi",
            "docker","vagrant","gitlfs","go","yum","conan","chef","puppet","generic"]), default='generic', required = True, show_default=True)
@click.option('-d', '--description')
@click.option('-i', '--includesPattern', type=str, default='**/*', show_default=True)
@click.option('-exp', '--excludesPatter', type=str, default='', show_default=True)
@click.option('-rl', '--repoLayoutRef', type=str, default='maven-2-default', show_default=True)
@click.option('-dtl', '--debianTrivialLayout', type=bool, default=False, show_default=True)
@click.option('-cpt', '--checksumPolicyType', type=click.Choice(['client-checksums','server-generated-checksums']), default='server-generated-checksums')
@click.option('-hr', '--handleReleases', type=bool, default=True, show_default=True)
@click.option('-hs', '--handleSnapshots', type=bool, default=True, show_default=True)
@click.option('-mxus', '--maxUniqueSnapshots', type=int, default=0, show_default=True)
@click.option('-mxut', '--maxUniqueTags', type=int, default=0, show_default=True)
@click.option('-snapvb', '--snapshotVersionBehavior', type=click.Choice(['unique', 'non-unique', 'deployer']), default='non-unique', show_default=True)
@click.option('-spcc', '--suppressPomConsistencyChecks', type=bool, default=False, show_default=True)
@click.option('-bo', '--blackedOut', type=bool, default=False, show_default=True)
@click.option('-xrayi', '--xrayIndex', type=bool, default=False, show_default=True)
@click.option('-ps', '--propertySets', type=click.Choice(['ps1', 'ps2']))
@click.option('-abe', '--archiveBrowsingEnabled', type=bool, default=False, show_default=True)
@click.option('-cym', '--calculateYumMetadata', type=bool, default=False, show_default=True)
@click.option('-yrd', '--yumRootDepth', type=int, default=0, show_default=True)
@click.option('-dav', '--dockerApiVersion', default='V2', show_default=True)
@click.option('-efli', '--enableFileListsIndexing', type=bool, default=False, show_default=True)
@click.option('-oicf', '--optionalIndexCompressionFormats', type=click.Choice(['bz2', 'lzma', 'xz']))
@click.option('-dr', '--downloadRedirect', type=bool, default=False, show_default=True)
@click.option('-bps', '--blockPushingSchema1', type=bool, default=False)
@click.option('-pr', '--priorityResolution', type=bool, default=False, show_default=True)

def create(key, packagetype, description, includespattern, excludespatter, repolayoutref, debiantriviallayout,checksumpolicytype, handlesnapshots, handlereleases, 
maxuniquesnapshots, maxuniquetags, snapshotversionbehavior, suppresspomconsistencychecks, blackedout,xrayindex, propertysets, archivebrowsingenabled, calculateyummetadata, yumrootdepth, dockerapiversion, enablefilelistsindexing, optionalindexcompressionformats, downloadredirect, blockpushingschema1, priorityresolution):
    """Creates a local new repository in Artifactory with the provided configuration. Supported only for local repositories. """

    endpoint = '/repositories/'+ key
    data = {
        'key': key,
        'rclass': 'local',
        'packageType': packagetype,
        'description': description,
        'includesPattern': includespattern,
        'excludesPatter': excludespatter,
        'repoLayoutRef': repolayoutref,
        'debianTrivialLayout' : debiantriviallayout,
        'checksumPolicyType': checksumpolicytype,
        'handleReleases': handlereleases,
        'handleSnapshots': handlesnapshots,
        'maxUniqueSnapshots': maxuniquesnapshots,
        'maxUniqueTags': maxuniquetags,
        'snapshotVersionBehavior': snapshotversionbehavior,
        'suppressPomConsistencyChecks': suppresspomconsistencychecks,
        'blackedOut': blackedout,
        'xrayIndex' : xrayindex,
        'propertySets': propertysets,
        'archiveBrowsingEnabled' : archivebrowsingenabled,
        'calculateYumMetadata' : calculateyummetadata,
        'yumRootDepth' : yumrootdepth,
        'dockerApiVersion' : dockerapiversion,
        'enableFileListsIndexing' : enablefilelistsindexing,
        'optionalIndexCompressionFormats' : optionalindexcompressionformats,
        'downloadRedirect' : downloadredirect,
        'blockPushingSchema1': blockpushingschema1,
        'priorityResolution': priorityresolution

    }
    response = Api.put_call(endpoint, data)
    click.echo(response.text)


# --- Update Repository command --- #
@cli.command()
@click.option('-k', '--key', type=str, required=True)
@click.option('-p', '--packageType', type=click.Choice( ["maven","gradle","ivy","sbt","helm","cocoapods",
            "opkg","rpm", "nuget","cran","gems","npm","bower","debian","composer","pypi",
            "docker","vagrant","gitlfs","go","yum","conan","chef","puppet","generic"]), default='generic', required = True, show_default=True)
@click.option('-d', '--description')
@click.option('-n', '--notes', type=str)
@click.option('-i', '--includesPattern', type=str, default='**/*', show_default=True)
@click.option('-exp', '--excludesPatter', type=str, default='', show_default=True)
@click.option('-rl', '--repoLayoutRef', type=str, default='maven-2-default', show_default=True)
@click.option('-dtl', '--debianTrivialLayout', type=bool, default=False, show_default=True)
@click.option('-cpt', '--checksumPolicyType', type=click.Choice(['client-checksums','server-generated-checksums']), default='server-generated-checksums')
@click.option('-hr', '--handleReleases', type=bool, default=True, show_default=True)
@click.option('-hs', '--handleSnapshots', type=bool, default=True, show_default=True)
@click.option('-mxus', '--maxUniqueSnapshots', type=int, default=0, show_default=True)
@click.option('-mxut', '--maxUniqueTags', type=int, default=0, show_default=True)
@click.option('-snapvb', '--snapshotVersionBehavior', type=click.Choice(['unique', 'non-unique', 'deployer']), default='non-unique', show_default=True)
@click.option('-spcc', '--suppressPomConsistencyChecks', type=bool, default=False, show_default=True)
@click.option('-bo', '--blackedOut', type=bool, default=False, show_default=True)
@click.option('-xrayi', '--xrayIndex', type=bool, default=False, show_default=True)
@click.option('-ps', '--propertySets', type=click.Choice(['ps1', 'ps2']))
@click.option('-abe', '--archiveBrowsingEnabled', type=bool, default=False, show_default=True)
@click.option('-cym', '--calculateYumMetadata', type=bool, default=False, show_default=True)
@click.option('-yrd', '--yumRootDepth', type=int, default=0, show_default=True)
@click.option('-dav', '--dockerApiVersion', default='V2', show_default=True)
@click.option('-efli', '--enableFileListsIndexing', type=bool, default=False, show_default=True)
@click.option('-oicf', '--optionalIndexCompressionFormats', type=click.Choice(['bz2', 'lzma', 'xz']))
@click.option('-dr', '--downloadRedirect', type=bool, default=False, show_default=True)
@click.option('-bps', '--blockPushingSchema1', type=bool, default=False)
@click.option('-pr', '--priorityResolution', type=bool, default=False, show_default=True)

def update(key, packagetype, description, notes, includespattern, excludespatter, repolayoutref, debiantriviallayout,checksumpolicytype, handlesnapshots, handlereleases, 
maxuniquesnapshots, maxuniquetags, snapshotversionbehavior, suppresspomconsistencychecks, blackedout,xrayindex, propertysets, archivebrowsingenabled, calculateyummetadata, yumrootdepth, dockerapiversion, enablefilelistsindexing, optionalindexcompressionformats, downloadredirect, blockpushingschema1, priorityresolution):
    """ Updates an local exiting repository configuration in Artifactory with the provided configuration elements. Supported for local repository only!"""

    endpoint = '/repositories/'+ key
    data = {
        'key': key,
        'rclass': 'local',
        'notes': notes,
        'packageType': packagetype,
        'description': description,
        'includesPattern': includespattern,
        'excludesPatter': excludespatter,
        'repoLayoutRef': repolayoutref,
        'debianTrivialLayout' : debiantriviallayout,
        'checksumPolicyType': checksumpolicytype,
        'handleReleases': handlereleases,
        'handleSnapshots': handlesnapshots,
        'maxUniqueSnapshots': maxuniquesnapshots,
        'maxUniqueTags': maxuniquetags,
        'snapshotVersionBehavior': snapshotversionbehavior,
        'suppressPomConsistencyChecks': suppresspomconsistencychecks,
        'blackedOut': blackedout,
        'xrayIndex' : xrayindex,
        'propertySets': propertysets,
        'archiveBrowsingEnabled' : archivebrowsingenabled,
        'calculateYumMetadata' : calculateyummetadata,
        'yumRootDepth' : yumrootdepth,
        'dockerApiVersion' : dockerapiversion,
        'enableFileListsIndexing' : enablefilelistsindexing,
        'optionalIndexCompressionFormats' : optionalindexcompressionformats,
        'downloadRedirect' : downloadredirect,
        'blockPushingSchema1': blockpushingschema1,
        'priorityResolution': priorityresolution

    }
    
    response = Api.post_call(endpoint, data)
    click.echo(response.text)


