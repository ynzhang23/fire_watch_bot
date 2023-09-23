%% 
filePath = fullfile('fire_dataset');
% Define the target size
targetSize = [224, 224, 3];

% Create an imageDatastore for the original images
imds = imageDatastore(filePath, ...
    'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames');

% Create a custom ReadFcn to resize and preprocess images
imds.ReadFcn = @(filename) preprocessAndResizeImage(filename, targetSize);

% Split the resized data into training, validation, and test sets
[trainDS, valDS, testDS] = splitEachLabel(imds, 0.7, 0.15, 0.15, 'randomized');

% Custom preprocessing function
function img = preprocessAndResizeImage(filename, targetSize)
    % Read the image
    img = imread(filename);

    % Resize the image to the target size
    img = imresize(img, targetSize(1:2));

    % Ensure the image has 3 color channels (e.g., convert grayscale to RGB)
    if size(img, 3) == 1
        img = cat(3, img, img, img); % Convert to RGB
    end
end

%%
