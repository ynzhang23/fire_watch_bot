inputSize = trainedNetwork_1.Layers(1).InputSize(1:2);
resizedTestDS = augmentedImageDatastore(inputSize, testDS);

[labels, scores] = classify(trainedNetwork_1, resizedTestDS);

accuracy = sum(labels == testDS.Labels)/numel(labels);
cm = confusionchart(labels, testDS.Labels);
cm.RowSummary = 'row-normalized';
cm.Title = 'Food Classification Confusion Matrix';