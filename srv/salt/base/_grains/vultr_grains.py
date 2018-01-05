import urllib2
def vultr_check():
# instantiate grains dictionary
# salt-call grains.items
    a = "test"
    grains = {}
# instantiate grains key cloud info

    try:
        grains ['cloud_info'] = []
        base_url = 'http://169.254.169.254/v1'
        instance_id = urllib2.urlopen(base_url + '/instanceid')
        instance_region_code =  urllib2.urlopen(base_url + '/region/regioncode')
        instance_id = instance_id.read()
        instance_region_code = instance_region_code.read()
        grains['cloud_info'].append({'provider': 'Vultr'})
        grains['cloud_info'][0]['instance_id'] = instance_id
        grains['cloud_info'][0]['instance_region_code'] = instance_region_code
        return grains
    except urllib2.URLError: #if the webpage is incorrect it will return false instead of error
        return False
    #print grains

if __name__ == '__main__':
    vultr_check()
