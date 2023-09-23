function predictLabel = predictFire(imagePath)
model = load('model2.mat');
img = imread(imagePath);
targetSize = [224, 224, 3];
% Resize the image to the target size
img = imresize(img, targetSize(1:2));
% Ensure the image has 3 color channels (e.g., convert grayscale to RGB)
if size(img, 3) == 1
    img = cat(3, img, img, img); % Convert to RGB
end
label = classify(model.temp, img);
predictLabel = char(label);
end