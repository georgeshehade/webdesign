Plotly.d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/alpha_shape.csv', function(err, rows){

    function unpack(rows, key) {
        console.log(rows.map(function(row) { return row[key]; }))
        return rows.map(function(row) { return row[key]; });
    }

    var data = [{
        x: [0.1592569, -0.0006548817, -0.06729978, 0.008771554, 0.1053525, 0.0007332899, 0.06969465, -0.15581682, -0.023337448, -0.13581109, -0.025528187, 0.12891644, -0.12288216, 0.005794851, 0.055143137, 0.13161848, -0.056270998, 0.08166748, -0.1218939, 0.12533404, 0.06134297, 0.09032887, 0.07943953, 0.1069307, -0.058140118, -0.13537587, 0.02636218, 0.09330067, -0.15484495, -0.02886381, 0.07662069, -0.044406183, 0.09595328, -0.036455188, -0.12732887, -0.03679945, -0.13799126, 0.15511677, -0.14611548, -0.12569427, -0.12495038, -0.08795278, -0.1374565],
        y: [0.15244676, -0.15709367, -0.12947983, -0.0006007569, -0.13352878, -0.10982176, -0.031318836, -0.08359552, -0.05795471, 0.027569473, -0.14705189, -0.16612828, -0.1488833, 0.015648358, -0.07696351, -0.0282594, -0.09917982, 0.10532373, -0.02895461, 0.086949624, -0.1542165, -0.082268335, 0.13426149, -0.051252216, -0.10614063, -0.14726438, -0.09880531, -0.14158429, -0.005122918, 0.07036432, 0.07989098, -0.07693458, -0.105170906, 0.12568238, 0.06823755, -0.08576811, 0.024898961, -0.02056714, 0.044052392, -0.08056192, 0.052910298, -0.15996455, -0.06032169],
        z: [-0.0524861, -0.026348533, 0.10677229, 0.09696157, 0.08152037, -0.12901606, 0.056010053, -0.05356929, -0.14759324, -0.059744496, 0.009458609, -0.027808798, 0.117454596, 0.13870932, -0.035224583, 0.1016659, -0.14009832, -0.0077587655, 0.033176325, 0.1290705, -0.0058616595, -0.029320175, 0.11103511, -0.103624724, -0.09303532, 0.113154255, 0.060932916, -0.031996157, -0.026202874, 0.08726476, 0.05828969, -0.037315868, -0.095809974, -0.0785048, -0.05285755, 0.015932824, 0.10726537, 0.1018745, 0.10331601, 0.0051411027, -0.049771238, 0.03673843, -0.1364823],
        mode: 'markers',
        type: 'scatter3d',
        name: 'Values',
        text: ["Accepting", "Ambitious", "Authentic",
        "Brave", "Caring", "Challenging", "Cheerful",
        "Collaborative", "Communicator", "Creative", "Curious",
        "Decisive", "Dedicated", "Detailed", "Determined",
        "Enthusiastic", "Flexible", "Friendly", "Funny",
        "Hard-working", "Helpful", "Honest", "Integrity",
        "Kind", "Leader", "Logical", "Loyal",
        "Motivated", "Nurturing", "Open-minded", "Optimistic",
        "Persistent", "Practical", "Problem-solver", "Resilient",
        "Responsible", "Self-controlled", "Strong", "Supportive",
        "Team-player", "Trustworthy", "Versatile", "Well-organised"],
        marker: {
          color: 'rgb(23, 190, 207)',
          size: 5
        }
    },{
        x: [-0.02052666, 0.06492347, -0.0342036, -0.1250352, -0.05051371],
        y: [-0.06595708, -0.00064844, 0.05239211, -0.0201957, 0.02671735],
        z: [0.02392972, -0.02657856, -0.05075364, 0.07142147, 0.02023248],
        mode: 'markers',
        type: 'scatter3d',
        name: 'Cluster Centroids',
        text: ["cluster1", "cluster2", "cluster3", "cluster4", "cluster5"],
        marker: {
            color: 'rgb(250, 0, 0)',
            size: 9
        }
    }];

    var layout = {
        autosize: true,
        height: 600,
        scene: {
            aspectratio: {
                x: 1,
                y: 1,
                z: 1
            },
            camera: {
                center: {
                    x: 0,
                    y: 0,
                    z: 0
                },
                eye: {
                    x: 1.25,
                    y: 1.25,
                    z: 1.25
                },
                up: {
                    x: 0,
                    y: 0,
                    z: 1
                }
            },
            xaxis: {
                type: 'linear',
                zeroline: false
            },
            yaxis: {
                type: 'linear',
                zeroline: false
            },
            zaxis: {
                type: 'linear',
                zeroline: false
            }
        },
        // title: '3d value clustering',
        width: 700
    };

    Plotly.newPlot('chart', data, layout);

})