from bokeh.models import CustomJS
from bokeh.models import CustomJSFilter
    
def input_callback(plot, source, out_text, topics, num_clusters): 

    # slider call back for cluster selection
    callback = CustomJS(args=dict(p=plot, source=source, out_text=out_text, topics=topics, num_clusters=num_clusters), code="""

                var key = text.value;
                var cluster = slider.value;
                var data = source.data; 

                var x = data['x'];
                var y = data['y'];
                var x_backup = data['x_backup'];
                var y_backup = data['y_backup'];

                var labels = data['desc'];

                var abstract = data['abstract'];
                var titles = data['titles'];
                var authors = data['authors'];
                var journal = data['journal'];

                if (cluster == num_clusters) {
                    out_text.text = 'Slide to specific cluster see it in more detail.';
                    for (var i = 0; i < x.length; i++) {
                        if(abstract[i].includes(key) || 
                        titles[i].includes(key) || 
                        authors[i].includes(key) || 
                        journal[i].includes(key)) {
                            x[i] = x_backup[i];
                            y[i] = y_backup[i];
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }
                else {
                    out_text.text = 'Titles of 5 representative papers ' + topics[Number(cluster)];
                    for (var i = 0; i < x.length; i++) {
                        if(labels[i] == cluster) {
                            if(abstract[i].includes(key) || 
                            titles[i].includes(key) || 
                            authors[i].includes(key) || 
                            journal[i].includes(key)) {
                                x[i] = x_backup[i];
                                y[i] = y_backup[i];
                            } else {
                                x[i] = undefined;
                                y[i] = undefined;
                            }
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }


            source.change.emit();
            """)
    return callback

js_filter_points_code = """
var is_checked = checkboxes.active.includes(0);

var indices = [];
for(var i=0; i<labels.length; i++){
    // Ignore outliers if the box is checked
    if(is_checked){
        if (labels[i] != "-1"){
            indices.push(i);
        }
    }
    else {
        indices.push(i);
    }
}
return indices;
"""

js_meta_filter_code = """
var cluster = slider.value;

var indices = [];
for(var i=0; i<labels.length; i++){
    if (labels[i] == cluster){
        indices.push(i);
    }
    }

return indices;
"""

def filter_callback(source):
    callback = CustomJS(args=dict(source=source), code="""
    source.change.emit();
    """)
    return callback
    
